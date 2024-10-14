# Circle Detection API

This project aims to detect circles in images using a pre-trained machine learning model - Florence2, providing detailed information such as bounding boxes, center points, and radius of each detected circle.

## Solution

This project implements an advanced circle detection system using Microsoft's Florence2 model, a state-of-the-art vision model that combines natural language understanding with computer vision capabilities. Our solution provides:

1. Accurate circle detection and counting in images
2. A user-friendly API for easy integration
3. Comprehensive evaluation metrics to assess model performance

By leveraging Florence2, we aim to overcome common challenges in circle detection, making our system robust across various scenarios.

## Key Features

- Image upload and storage in persistent storage
- Unique identifier assignment for each detected circular object
- Retrieval of circular objects with their bounding boxes
- Calculation of bounding box, centroid, and radius for each circular object
- Model/algorithm evaluation strategy
- Containerized solution for easy deployment

## Implementation Details

The solution is based on Python and utilizes various computer vision libraries. Here's a brief overview of the main components:

- **Image Upload Endpoint** - `POST /upload_image/`: Allows users to upload images and stores them in persistent storage. Also circles detection, assigning them unique identifiers, and calculating details like center point, radius takes place when this api is hit. These details are stored in the database.
- **Visualization** - `POST /get_annotated_circle_image/`: Displays the original image and the segmentation mask in the same window.
- **Object Retrieval** - `POST /get_circle_data/`: Provides an endpoint to retrieve a list of all circular objects with their bounding boxes. Also `POST /get_circle_properties/` allows to get details about specific circle of the given image as we pass its name.
- **Model Evaluation**: Model evaluated on how good the model is. Please check `model_evaluation` folder. Results are described in depth in the README file.

Also check out the README files under each of the folders for further implementation details.

## Project Structure

```bash
├── circle_detector
│   ├── detector.py
│   ├── __init__.py
│   └── README.md
├── config
│   ├── constants.py
│   ├── __init__.py
│   └── README.md
├── custom_logger
│   ├── helper.py
│   ├── __init__.py
│   └── README.md
├── data
│   ├── coin-dataset
│   │   ├── 001_jpg.rf.68d4fff5cb81c9ade16111b4434e2090.jpg
│   │   ├── 00334d13-4962-4b53-9dd2-121f8f000beb_jpg.rf.241a52973871ddcbfacc334c19c47b0d.jpg
│   │   ├── 0044de2f-d45b-4526-99eb-adf982d98b05_jpg.rf.2140f29410c7dad67cfd6b952645a3fb.jpg
│   │   ...
│   ├── model_eval_data
│   │   ├── circle_counts_florence.csv
│   │   └── circle_counts_ground_truth.csv
│   ├── processed
│   │   └── circular_objects.db
│   ├── README.md
│   └── uploads
│       ├── 00db272e-1d5f-4ff1-9cd6-1d8be42cb1a5_jpg.rf.f5818b173262a6f187db2af748531648.jpg
│       ├── 170_1479423174_jpg.rf.4e5db24f633d230a3260c1d87a940134.jpg
│       ├── 175_1479423456_jpg.rf.0723ceef6a241da65f4f36db2132002b.jpg
│       ...
├── database
│   ├── db_manager.py
│   ├── __init__.py
│   └── README.md
├── docker-compose.yaml
├── Dockerfile
├── environment.yml
├── image_processing
│   ├── __init__.py
│   ├── README.md
│   └── visualization.py
├── main.py
├── model_evaluation
│   ├── evaluation.ipynb
│   ├── image_coin_counter.py
│   ├── README.md
│   └── result
│       ├── 4386a0c1-247f-4820-a5e5-b4a0f9e9db68.png
│       ├── 7e0364c7-d594-40a1-9da3-5dbddf6fc5aa.png
│       ├── d393bf02-94d9-433a-bc61-dde771539fa0.png
│       └── results.png
├── models
│   ├── __init__.py
│   ├── README.md
│   └── schemas.py
├── README.md
├── requirements.txt
└── service
    ├── app.py
    ├── __init__.py
    ├── README.md
    └── screenshots
        ├── 1.png
        └── 2.png
```

## Running the Project

### System Project was developed

This project makes use of GPU acceleration for model inference, though the usage is minimal as the model size is just 1.54GB. Below are the system specifications:

- CPU:
  - Family: 25
  - Model: 8
  - Model Name: AMD Ryzen Threadripper PRO 5975WX 32-Cores
- RAM: 64 GB
- VRAM: 24 GB x 2
- GPU Model: NVIDIA RTX-4090 x 2
- Ubuntu 22.04

### Locally

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/circle-detection-project.git
   cd circle-detection-project
   ```

2. Set up a virtual environment (optional but recommended):

   ```
   conda create -n circle_detection_project python=3.11
   conda activate circle_detection_project
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py
   ```

The server will start on `http://0.0.0.0:8188`.

### Using Docker

The project is containerized using Docker, making it easy to deploy and manage in various environments.

1. Ensure Docker and Docker Compose are installed on your system.

2. Build and run the Docker container:
   ```
   docker-compose up --build
   ```

The API will be available at `http://localhost:8188`.

## Acknowledgments

- Microsoft for the Florence2 model

For any questions or support, please open an issue in the GitHub repository.
