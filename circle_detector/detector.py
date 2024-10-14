import os
import sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
from custom_logger import logger
from config import MODEL_ID, TASK_PROMPT, TEXT_INPUT
from typing import Any, Dict, Optional


class CircleDetector:
    def __init__(self, model_id: str = MODEL_ID) -> None:
        """
        Initialize the CircleDetector class and load the model.

        Args:
            model_id (str): The model to use for circle detection.
        """
        logger.info(f"Loading model: {model_id}...")
        try:
            self.model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).eval()
            self.processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
            logger.info("Model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load model '{model_id}': {e}")
            raise RuntimeError(f"Model loading failed: {e}")

    def detect_circles(self, task_prompt: str, image: Image.Image, text_input: Optional[str] = None) -> Dict[str, Any]:
        """
        Use the Florence-2 model to detect circles in an image.

        Args:
            task_prompt (str): The task prompt to use for the model.
            image (Image.Image): The image to detect circles in.
            text_input (Optional[str], optional): An optional text string to append to the task prompt. Defaults to None.

        Returns:
            Dict[str, Any]: The parsed output of the model, containing the bounding boxes of the detected circles, and label.
        """
        if text_input is None:
            prompt = task_prompt
        else:
            prompt = task_prompt + text_input
        logger.debug(f"Generated prompt: {prompt}")

        try:
            inputs = self.processor(text=prompt, images=image, return_tensors="pt")
            logger.info("Inputs processed successfully.")
        except Exception as e:
            logger.error(f"Error processing inputs: {e}")
            raise ValueError(f"Input processing failed: {e}")

        try:
            logger.info("Generating output from the model...")
            generated_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=1024,
                early_stopping=False,
                do_sample=False,
                num_beams=3,
            )
            logger.info("Model generation completed.")
        except Exception as e:
            logger.error(f"Error during model generation: {e}")
            raise ValueError(f"Model generation failed: {e}")

        try:
            generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
            logger.debug(f"Generated text: {generated_text}")
            parsed_answer = self.processor.post_process_generation(
                generated_text,
                task=task_prompt,
                image_size=(image.width, image.height),
            )
            return parsed_answer
        except Exception as e:
            logger.error(f"Error during post-processing: {e}")
            raise ValueError(f"Post-processing failed: {e}")

    def get_circle_data(self, image_path: str) -> Dict[str, Any]:
        """
        Get the required circle data from the detected circle bounding boxes by the model.
        Also, _calculate_circle_properties() is called to calculate the center point, radius, and count of the circles.
        
        Args:
            image_path (str): Path to the image file.

        Returns:
            Dict[str, Any]: A dictionary containing circle data including image name, circle count, and metadata - circle_id, bounding_box, center_point, radius.
        """
        try:
            image = Image.open(image_path)
            logger.info(f"Image '{image_path}' opened successfully.")
        except (IOError, FileNotFoundError) as e:
            logger.error(f"Failed to open image '{image_path}': {e}")
            raise RuntimeError(f"Image opening failed: {e}")

        result = self.detect_circles(
            task_prompt=TASK_PROMPT, image=image, text_input=TEXT_INPUT
        )[TASK_PROMPT]
        detailed_result = self._calculate_circle_properties(image_path, result)
        return detailed_result

    def _calculate_circle_properties(self, image_path: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate circle properties such as center point, radius, and count from the detection result.

        Args:
            image_path (str): Path to the image file.
            result (Dict[str, Any]): The result from the circle detection.

        Returns:
            Dict[str, Any]: A dictionary containing circle data including image name, circle count, and metadata - circle_id, bounding_box, center_point, radius.
        """
        bboxes = result.get("bboxes", [])
        labels = result.get("labels", [])

        circle_data = {
            "image_name": os.path.basename(image_path),
            "circle_count": len(bboxes),
            "metadata": [],
        }

        for idx, bbox in enumerate(bboxes):
            if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
                logger.warning(f"Invalid bounding box at index {idx}: {bbox}")
                continue

            x1, y1, x2, y2 = bbox
            center_x = (x1 + x2) / 2.0
            center_y = (y1 + y2) / 2.0
            radius = min(x2 - x1, y2 - y1) / 2.0

            circle_properties = {
                "circle_id": idx + 1,
                "bounding_box": bbox,
                "center_point": (center_x, center_y),
                "radius": radius,
            }

            if idx < len(labels):
                circle_properties["label"] = labels[idx]

            circle_data["metadata"].append(circle_properties)

        return circle_data

circle_detector = CircleDetector()