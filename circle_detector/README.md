# Circle Detector folder - `circle_detector`

This module provides functionality for detecting circular objects in images using a pre-trained model.

## Contents

- `CircleDetector` class: The main class for circle detection
- Necessary imports and configurations
- Logging setup
- Global variables for model configuration and instance

## Key Functions

1. `__init__(self, model_id: str = MODEL_ID) -> None`: Initializes the CircleDetector with a specified model.
2. `detect_circles(self, task_prompt: str, image: Image.Image, text_input: Optional[str] = None) -> Dict[str, Any]`: Detects circles and returns bounded boxes and respective labels in a given image using the model.
3. `get_circle_data(self, image_path: str) -> Dict[str, Any]`: Processes an image file and returns detailed circle data.
4. `_calculate_circle_properties(self, image_path: str, result: Dict[str, Any]) -> Dict[str, Any]`: Internal method to calculate circle properties from detection results. Here unique id is assigned to each circle of a given input image. Center point and radius are also calculated here.

## Global Variables

The module uses several global variables:

- `MODEL_ID`: The identifier for the pre-trained model used for detection.
- `TASK_PROMPT`: The prompt used to instruct the model for the circle detection task.
- `TEXT_INPUT`: Additional text input used in processing.

These variables are imported from the `utilities` module.

- `circle_detector`: A global instance of the `CircleDetector` class, created at the end of this file.

## Usage

### In Python scripts:

```python
from circle_detector import circle_detector

# Use the pre-initialized detector
image_path = "path/to/your/image.jpg"
circle_data = circle_detector.get_circle_data(image_path)

# Access the results
print(f"Image: {circle_data['image_name']}")
print(f"Number of circles detected: {circle_data['circle_count']}")
for circle in circle_data['metadata']:
    print(f"Circle ID: {circle['circle_id']}")
    print(f"Bounding Box: {circle['bounding_box']}")
    print(f"Center Point: {circle['center_point']}")
    print(f"Radius: {circle['radius']}")
    if 'label' in circle:
        print(f"Label: {circle['label']}")
    print("---")
```

### In API endpoints:

The `circle_detector` global instance is used in API endpoints. Refer to the API documentation for specific usage in endpoint implementations.

## Notes

- Ensure that the required dependencies are installed, the model is properly set up, and the global variables are correctly configured in the `utilities` module before using this module.
- The `circle_detector` instance is created once when this module is imported and reused across API calls for efficiency.
- The module uses type hinting for better code readability and maintainability.
- Logging is implemented throughout the module for debugging and monitoring purposes.
