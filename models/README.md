# Models - `models`

This folder contains the data models used primarily for request and response bodies in API endpoints.

## Contents

- `__init__.py`: Exports the model classes for easy import
- `schemas.py`: Defines the Pydantic models for data validation and serialization

## Model Definitions

### Request Models

1. `ImageName`
   - Fields:
     - `image_name: str`

2. `ImageCircleRequest` (extends `ImageName`)
   - Fields:
     - `image_name: str` (inherited)
     - `circle_id: int`

### Response Models

1. `CircleProperties`
   - Fields:
     - `circle_id: int`
     - `bounding_box: List[float]`
     - `center_point: List[float]`
     - `radius: float`

2. `CircleData`
   - Fields:
     - `image_name: str`
     - `circle_count: int`
     - `metadata: List[CircleProperties]`

## Usage

To use these models in your code:

```python
from models import CircleData, ImageCircleRequest

# For request validation
request_data = ImageCircleRequest(image_name="example.jpg", circle_id=1)

# For response formatting
circle_data = CircleData(
    image_name="example.jpg",
    circle_count=3,
    metadata=[
        CircleProperties(circle_id=1, bounding_box=[10, 10, 50, 50], center_point=[30, 30], radius=20),
        # ... more circle properties
    ]
)
```

## Notes

- These models use Pydantic, which provides runtime type checking and data validation.
- Ensure that Pydantic is installed in your project environment (`pip install pydantic`). Its already included in the `requirements.txt` file.
- When adding new models or modifying existing ones, make sure to update the exports in `__init__.py`.