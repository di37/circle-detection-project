from pydantic import BaseModel
from typing import List

# Request Bodies
class ImageName(BaseModel):
    image_name: str

class ImageCircleRequest(ImageName):
    circle_id: int 

# Response Bodies
class CircleProperties(BaseModel):
    circle_id: int
    bounding_box: List[float]
    center_point: List[float]
    radius: float

class CircleData(BaseModel):
    image_name: str
    circle_count: int
    metadata: List[CircleProperties]