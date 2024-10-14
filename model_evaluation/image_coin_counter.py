# Path Libraries
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import pandas as pd
from circle_detector import circle_detector
from custom_logger import logger

from config import CIRCLE_IMAGE_DIR, RESULT_CSV_PATH

# List to store results
image_paths = os.listdir(CIRCLE_IMAGE_DIR)
results = []

# Loop through all images in the directory
for idx, image_file in enumerate(image_paths):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  # Add or remove file extensions as needed
        image_path = os.path.join(CIRCLE_IMAGE_DIR, image_file)
        logger.info(f"Determining number of circles for image {idx+1} of {len(image_paths)}")
        result = circle_detector.get_circle_data(image_path)
        
        logger.info(result)
        # Collect only the image name and circle count
        results.append({
            'image_name': result['image_name'],
            'number_of_circles_pred': result['circle_count']
        })
        
df = pd.DataFrame(results)
df.to_csv(RESULT_CSV_PATH, index=False)