import os
from PIL import Image

def preprocess_images(input_dir, output_dir, size=(256, 256)):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(input_dir, filename))
            img = img.resize(size)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(os.path.join(output_dir, filename))

input_dir = r'C:\\Users\\Marx\\Desktop\\i.a giramile\\VeridianCode-AN\\imgs\\class1'
output_dir = r'C:\\Users\\Marx\\Desktop\\i.a giramile\\VeridianCode-AN\\imgs\\output'
preprocess_images(input_dir, output_dir)