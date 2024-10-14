# Path Libraries
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

# Image Processing
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os, io
from typing import List
import json 

from config import UPLOAD_DIR, FORMAT

def plot_bounding_boxes_and_mask(circle_data: List, image_name: str):
    # Load the image
    """
    Generates a plot of the detected circles on the given image and
    their corresponding masks.

    Args:
        circle_data (List): A list containing the image names, their circle count and metadata
            for each detected circle.
        image_name (str): The name of the image.

    Returns:
        io.BytesIO: A BytesIO buffer containing the generated plot image.
    """
    image_path = os.path.join(UPLOAD_DIR, image_name)
    image = Image.open(image_path)
    image_np = np.array(image)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    # Display the original image in the first subplot
    ax1.imshow(image_np)
    ax1.set_title('Detected Circles')
    ax1.axis('off')

    # Create a mask image
    mask = np.zeros(image_np.shape[:2], dtype=np.uint8)
    print()
    # Plot each bounding box and update the mask
    for circle_properties in json.loads(circle_data[1]):
        bbox = circle_properties['bounding_box']
        x1, y1, x2, y2 = bbox

        # Create a Rectangle patch
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1,
                                 linewidth=2, edgecolor='r', facecolor='none')

        # Add the rectangle to the Axes
        ax1.add_patch(rect)

        # Annotate with circle ID
        ax1.text(x1, y1 - 10, f"Circle ID: {circle_properties['circle_id']}", color='red', fontsize=12,
                 bbox=dict(facecolor='white', alpha=0.5))

        # Update the mask
        x1_int, y1_int, x2_int, y2_int = map(int, [x1, y1, x2, y2])
        mask[y1_int:y2_int, x1_int:x2_int] = 255

    # Display the mask in the second subplot
    ax2.imshow(mask, cmap='gray')
    ax2.set_title('Mask')
    ax2.axis('off')

    # Adjust layout and display the plot
    plt.tight_layout()
    
    # Save the figure to a buffer instead of displaying it
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format=FORMAT)
    plt.close(fig)  # Close the figure to free memory
    image_buffer.seek(0)
    return image_buffer

