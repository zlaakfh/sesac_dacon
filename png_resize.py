## pip install pillow

import os
from PIL import Image


yolo11n_size = (640, 640)
src_folder = "./hat"

dst_folder = src_folder + "_resize"

os.makedirs(dst_folder, exist_ok=True)

for root, dirs, files in os.walk(src_folder):
    for filename in files:
        if filename.lower().endswith(".png"):
            src_path = os.path.join(root, filename)

            img = Image.open(src_path)
            resized = img.resize(yolo11n_size)

            new_name = os.path.relpath(src_path, src_folder)  # 하위 폴더 구조 반영
            new_path = os.path.join(dst_folder, new_name)

            os.makedirs(os.path.dirname(new_path), exist_ok=True)

            resized.save(new_path)
            print(f"Saved: {new_path}")