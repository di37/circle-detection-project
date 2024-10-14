# Data Folder - `data`

This folder contains various data files and directories used in the project.

## Structure

- `processed/`
  - `circular_objects.db`: Database file for storing processed circle data of the images.
- `uploads/`
  - Contains uploaded image files (e.g., `00db272e-1d5f-4ff1-9cd6-1d8be42cb1a5_jpg.rf.f5818b173262a6f187db2af748531648.jpg`)
- `coin-dataset`: Dataset of images given with the assignment for model evaluation
- `model_eval_data`: This folder includes two csv files - `circle_counts_ground_truth.csv` and `circle_counts_florence.csv`.

## Contents

### Processed Data

The `processed` directory contains data that has been processed by the application:

- `circular_objects.db`: SQLite database file storing detected circle data from the images.

### Uploads

The `uploads` directory is used to store image files that have been uploaded to the system for processing. This will be our **persistant storage of the images**.

### Model Evaluation Data

`circle_counts_ground_truth.csv` - manually counted coins for each image  and `circle_counts_florence.csv` - automated counts of coins for each image in the `coin-dataset` folder. This will be used to evaluate the performance of the model.

## Coin Dataset

This includes 191 images of coins at various conditions for proper model evaluation but we are using the term - circle as mentioned in the assignment. 

## Usage

- Uploaded images are stored in the `uploads` directory.
- After processing, results are stored in the `circular_objects.db` file.
- Ensure proper read/write permissions are set for the application to access these directories and files.