# Brain-tumour-identification-from-uploaded-MRI-scans-using-ResUnet-ATTP-and-Unet
Brain tumour identification from uploaded MRI scans using ResUNet-ATTP and U-Net deep learning models. The system analyses MRI images, segments potential tumour regions, and visualizes the results to support medical image analysis and research.

# Brain Tumour Identification from Uploaded MRI Scans Using ResUNet-ATTP and U-Net

## Project Description

This project is a deep learning-based application for brain tumour identification using uploaded Magnetic Resonance Imaging (MRI) scans. It uses image processing techniques and a prediction module to analyse MRI images and identify potential tumour presence.

The application is developed using Python and Flask, providing a web interface where users can upload MRI images, view processed images, and obtain prediction results.

## Features

- **MRI Image Upload:** Upload brain MRI scans through the web interface.
- **Image Preprocessing:** Reduce image noise to prepare MRI scans for analysis.
- **Tumour Visualization:** Display processed images and segmentation results.
- **Tumour Prediction:** Predict whether a tumour is detected in the uploaded image.
- **Confidence Output:** Display the prediction confidence score.
- **Web Interface:** Interact with the application through a Flask-based interface.

## Technologies Used

- Python
- Flask
- OpenCV
- Deep Learning
- ResUNet-ATTP
- U-Net
- HTML and CSS for the web interface

*Note: The exact model architecture and frontend technologies should be verified against the implementation files.*

## Project Structure

```text
Brain-Tumour-Identification/
├── model/
├── static/
│   ├── result/
│   └── uploads/
├── templates/
├── test images/
├── app.py
├── displayTumor.py
├── predictTumor.py
└── README.md
```

The application code saves uploaded images and generated results under `static/results/`. Update the folder structure above if your repository uses different directory names.

## Installation and Setup

### Prerequisites

- Python 3.x
- pip
- Required model files and dependencies

### Steps to Run

1. Clone the repository:

   ```bash
   git clone <https://github.com/shrina-02/Brain-tumour-identification-from-uploaded-MRI-scans-using-ResUnet-ATTP-and-Unet.git>
   ```

2. Navigate to the project directory:

   ```bash
   cd <PROJECT-DIRECTORY>
   ```

3. Install the basic application dependencies:

   ```bash
   pip install Flask opencv-python
   ```

   Install any additional dependencies required by the prediction model.

4. Ensure the required model files are available in the `model/` directory and the necessary Python modules are present.

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Open the local URL displayed in the terminal, usually `http://127.0.0.1:5000/`.

## How to Use

1. Start the Flask application.
2. Open the application in your web browser.
3. Upload a brain MRI image.
4. Select the available image-processing option to view the processed image.
5. Run the prediction option to obtain the tumour identification result.
6. Review the displayed prediction and confidence score.

## Applications

- Brain MRI image analysis research
- Medical image processing
- Deep learning experimentation
- Educational projects in healthcare AI

## Disclaimer

This project is intended for educational and research purposes only. Its predictions are not a substitute for professional medical diagnosis. All results should be evaluated by qualified healthcare professionals.
