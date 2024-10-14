# Path Libraries
import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

# Directory to store uploaded images
UPLOAD_DIR = "data/uploads"
CIRCLE_IMAGE_DIR = 'data/coin-dataset/'
DATABASE_PATH = "data/processed/circular_objects.db"
PREDICTED_COUNT_CSV_PATH = 'data/model_eval_data/circle_counts_florence.csv'
TRUE_COUNT_CSV_PATH = 'data/model_eval_data/circle_counts_ground_truth.csv'

FORMAT = "png"
MODEL_ID = "microsoft/Florence-2-large"
TASK_PROMPT = "<CAPTION_TO_PHRASE_GROUNDING>"
TEXT_INPUT = "circle"