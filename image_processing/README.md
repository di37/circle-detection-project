# Image Processing - `image_processing`

This folder contains functions for processing and visualizing images, particularly for the circular object detection project.

## Contents

- `__init__.py`: Exports the `plot_bounding_boxes_and_mask` function for easy import
- `visualization.py`: Contains functions for visualizing detected circles and their masks

## Visualization Functions

### `plot_bounding_boxes_and_mask(circle_data: List, image_name: str) -> io.BytesIO`

This function generates a plot of the detected circles on a given image and their corresponding masks.

Parameters:
- `circle_data` (List): Contains image names, circle count, and metadata for each detected circle
- `image_name` (str): Name of the image file

Returns:
- `io.BytesIO`: A buffer containing the generated plot image

The function creates a figure with two subplots:
1. Original image with bounding boxes and circle IDs
2. Binary mask of the detected circles

## Usage

To use the image processing functions in your code:

```python
from image_processing import plot_bounding_boxes_and_mask

# Using the visualization function
image_name = "example.jpg"
circle_data = [...] # Your circle data here
image_buffer = plot_bounding_boxes_and_mask(circle_data, image_name)

# You can then use this buffer to save or display the image
```

## Configuration

The module uses the following configuration variables from the `config` module:
- `UPLOAD_DIR`: Directory where uploaded images are stored
- `FORMAT`: Image format for saving (e.g., "png")

Ensure these are properly set in your project's configuration.

## Notes

- The `plot_bounding_boxes_and_mask` function assumes that the input `circle_data` is in the correct format. Make sure the data structure matches the expected input.
- The function uses matplotlib to create visualizations. Ensure that matplotlib is properly configured for your environment, especially if running in a non-interactive setting.
- The generated image is returned as a BytesIO buffer, which can be easily saved to a file or served directly in a web application.
- Remember to close the returned buffer after use to free up system resources.