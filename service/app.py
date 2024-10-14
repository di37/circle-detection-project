import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import json 

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

from custom_logger import logger

from database import circle_database
from circle_detector import circle_detector

from image_processing import plot_bounding_boxes_and_mask
from config import UPLOAD_DIR

from models import CircleProperties, CircleData, ImageName, ImageCircleRequest

# Create the FastAPI app
app = FastAPI()

# Endpoint to upload image and store it in persistent storage
@app.post("/upload_image/")
async def aupload_image(file: UploadFile = File(...)):
    """
    Endpoint to upload image and store it in persistent storage.

    Args:
        file (UploadFile): The image file to be uploaded.

    Returns:
        dict: A dictionary containing a success message.

    Raises:
        HTTPException: If the image file already exists.

    """
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    
    if not os.path.isfile(image_path):
        with open(image_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Detect circles in the uploaded image
        circle_data = circle_detector.get_circle_data(image_path)
        # Store the circle data in the database for uploaded image
        circle_database.store_circle_data(**circle_data)
        return {"message": f"Image '{file.filename}' uploaded successfully."}
    else:
        logger.info(f"Image '{file.filename}' already exists. Skipping circle detection.")
        return {"message": f"Image '{file.filename}' already exists. Skipping circle detection."}

# Endpoint to retrieve the processed image with bounding boxes and masks that has been uploaded and stored in persistent storage
# and its information about the circles is stored in the database
@app.post("/get_annotated_circle_image/")
async def aget_annotated_circle_image(image_name: ImageName):
    """
    Endpoint to retrieve the processed image with bounding boxes and masks.

    Args:
        image_name (str): The name of the image.

    Returns:
        StreamingResponse: The processed image with bounding boxes and masks.
    """
    circle_data = circle_database.get_circle_data_db(image_name.image_name)
    if circle_data:
        # Generate the image buffer
        image_buffer = plot_bounding_boxes_and_mask(circle_data, image_name.image_name)
        return StreamingResponse(image_buffer, media_type="image/png")
    else:
        raise HTTPException(status_code=404, detail="Image name not found. Please upload again.")

# Endpoint to retrieve list of all circular objects (id and bounding box) for queried image
@app.post("/get_circle_data/", response_model=CircleData)
async def aget_circle_data(image_name: ImageName):
    """
    Endpoint to retrieve list of all circular objects (id and bounding box) for queried image.

    Args:
        image_name (str): The name of the image.

    Returns:
        CircleData: Contains the image name, number of circular objects, and metadata for each object.
    """
    circle_data = circle_database.get_circle_data_db(image_name.image_name)
    # Conversion of Tuple to Dictionary
    if circle_data:
        circle_data = {
            "image_name": image_name.image_name,
            "circle_count": circle_data[0],
            "metadata": json.loads(circle_data[1])
        }
        return circle_data
    else:
        raise HTTPException(status_code=404, detail="Image name not found. Please upload again.")

# Endpoint to find bounding box, centroid and radius for queried circular object.
@app.post("/get_circle_properties/", response_model=CircleProperties)
async def aget_circle_properties(image_circle_request: ImageCircleRequest):
    
    """
    Endpoint to retrieve the properties (bounding box, centroid and radius) of the queried circular object.

    Args:
        image_circle_request (ImageCircleRequest): The image name and object id of the queried circular object.

    Returns:
        CircleProperties: Contains the bounding box, centroid and radius of the queried circular object.
    """
    circle_data = circle_database.get_circle_data_db(image_circle_request.image_name)
    # Getting the circle detail of a specific circle from the queried image
    if circle_data:
        metadata = json.loads(circle_data[1])
        for obj in metadata:
            if obj["circle_id"] == image_circle_request.circle_id:
                return CircleProperties(**obj)
        raise HTTPException(status_code=404, detail="Object ID not found")
    else:
        raise HTTPException(status_code=404, detail="Image name not found")

# Endpoint to get the processed image with bounding boxes and masks