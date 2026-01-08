import os
import json
import cv2
import numpy as np

# Input and output folders
input_folder = "./img"
output_folder = "./label"
os.makedirs(output_folder, exist_ok=True)

# Define class-specific colors (BGR format)
class_colors = {
    "car": (0, 255, 0),
    "tree": (0, 0, 255),
    "traffic sign": (255, 0, 0),
    "building": (255, 255, 0)
}

# Iterate over JSON files in the input folder
for file_name in os.listdir(input_folder):
    if not file_name.endswith(".json"):
        continue

    json_path = os.path.join(input_folder, file_name)
    with open(json_path, "r") as f:
        data = json.load(f)

    width, height = data["imageWidth"], data["imageHeight"]
    mask = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw each labeled shape
    for shape in data["shapes"]:
        points = np.array(shape["points"], dtype=np.int32)
        class_name = shape.get("label")

        if class_name not in class_colors:
            raise ValueError(f"Color for class '{class_name}' is not defined.")

        cv2.fillPoly(mask, [points], color=class_colors[class_name])

    # Save the mask image
    base_name = os.path.splitext(data["imagePath"])[0]
    output_path = os.path.join(output_folder, f"{base_name}.png")
    cv2.imwrite(output_path, mask)

print("Done: All JSON files have been converted to RGB masks!")
