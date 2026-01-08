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

## Project Structure

The folder structure of this project is organized as follows:

```text
labelme-usage/
├── img/                   # Original images for annotation (.jpg, .png)
│   ├── sample_image1.jpg
│   ├── sample_image1.json # Labelme JSON annotation file (generated after annotation)
│   ├── sample_image2.jpg
│   └── sample_image2.json
├── label/                 # Generated labeling images
│   ├── sample_image1.png
│   └── sample_image2.png
├── json_to_labeling.py    # Utility script to convert JSON to labeling images
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

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

## Usage

Follow the steps below to annotate images and generate labeling images using Labelme.

---

1. **Load Images**
When the Labelme window opens, click **Open** or **Open Dir** to load an image or an image directory.

2. **Draw Annotations**
Once an image is displayed, select a desired labeling tool from the left toolbar, such as:
Use the selected tool to draw annotations on the image.

- **Polygons**
- **Rectangle**
- ...
- **AI-Polygon**
- **AI-Mask**

3. **Assign Class Labels**
   1. Select the annotated shape.
   2. Double-click the shape to assign a label.
   3. Enter the class name (e.g., `car`, `person`, `object`) and confirm.

4. **Save Annotations**
   Click the **`Save`** button to store the annotation.
   After saving, a corresponding **`.json`** file will be created in the image directory, containing the annotation and label information.

```text
img/
 ├── sample_image.jpg
 └── sample_image.json
 ```

5. **Generate Labeling Images from JSON**
After saving your annotations, you can convert the JSON files into labeling images.
This will create a corresponding labeling image in the label folder for each JSON file, with the same filename and image size as the original.

Note: The class-to-color mapping in the labeling images may need to be adjusted according to your project requirements.

Run the following command in your environment:
   ```bash
   python json_to_labeling.py
