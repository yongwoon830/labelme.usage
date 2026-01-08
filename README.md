# labelme.usage

<img width="385" height="385" alt="Demo Screenshot" src="https://github.com/user-attachments/assets/952abbdf-e055-44c3-a3c4-08625c68da11" />

This repository demonstrates how to create simple training data for image segmentation using a GUI-based labeling approach.  
The workflow is based on [Labelme](https://github.com/wkentaro/labelme), a popular open-source annotation tool.

Using Labelme, users can easily annotate images with polygon-based labels through a graphical interface, making it suitable for preparing segmentation datasets for machine learning and deep learning models.

---

## Description
This project demonstrates a GUI-based approach for annotating images with polygons, allowing users to quickly create datasets for image segmentation model training.

---

## Test Environment
- OS: Windows 11 / Ubuntu 22.04
- Python: 3.9
- Labelme version: 5.2.0
- Additional packages: numpy, opencv-python

---

## Installation & Run

Follow the steps below to set up the project environment using Anaconda:

1. **Download Anaconda**  
   Download and install Anaconda from the official website: [https://www.anaconda.com/download/success#download](https://www.anaconda.com/download/success#download)

2. **Open Anaconda Prompt**  
   Launch the Anaconda Prompt application to execute the following commands.

3. **Create a Virtual Environment**  
   Create a dedicated environment named `labelme` with Python 3.9:
   ```bash
   conda create -n labelme python==3.9 -y

4. **Activate the Virtual Environment**  
   ```bash
   conda activate labelme
   cd labelme

5. **Install Required Libraries**
   Install all necessary dependencies from the requirements.txt file:
   ```bash
   conda install pyqt -y
   pip install -r requirements.txt

6. **Run Labelme**
   Launch the Labelme GUI from the Anaconda Prompt:
   ```bash
   labelme
