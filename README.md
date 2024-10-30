# Image Masking Processor

This project utilizes OpenCV to read JPEG images from a specified directory, create binary mask images where all three color channels are above a certain threshold, and save the mask images as lossless files. The program also counts and logs the total number of high-intensity pixels across all processed images.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Output Directory](#output-directory)
- [License](#license)

## Features

- Reads JPEG images from a specified folder.
- Creates binary mask images based on pixel intensity.
- Outputs mask images in a specified directory.
- Logs the total count of high-intensity pixels from all images.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

You can install the required packages using pip:

```bash
pip install opencv-python numpy
