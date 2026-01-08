# labelme.usage

<img width="385" height="385" alt="Demo Screenshot" src="https://github.com/user-attachments/assets/952abbdf-e055-44c3-a3c4-08625c68da11" />

This repository demonstrates how to create simple training labeling data for image segmentation using a GUI-based approach.  
The workflow is based on [Labelme](https://github.com/wkentaro/labelme), a popular open-source annotation tool.

Using Labelme, users can easily annotate images with polygon-based labels through a graphical interface, making it suitable for preparing segmentation datasets for machine learning and deep learning models.

---

## Description
This project demonstrates a GUI-based approach for annotating images with polygons, allowing users to quickly create datasets for image segmentation model training.

---

## Test Environment
- OS: Windows 11 / Anaconda prompt(miniconda3)
- Python: 3.9.25

---

## Installation
```bash
# 1. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 2. Install required packages
pip install labelme numpy opencv-python
