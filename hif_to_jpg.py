import pyheif
from PIL import Image
import os

input_directory = 'hif_firectory'
output_directory = 'jpg_directory'

os.makedirs(output_directory, exist_ok=True)

for file_name in os.listdir(input_directory):
    if file_name.lower().endswith('.hif') or file_name.lower().endswith('.heif') or file_name.lower().endswith('.heic'):
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(output_directory, os.path.splitext(file_name)[0] + '.jpg')
        
        # Read the .hif file
        heif_file = pyheif.read(input_path)
        
        # Convert to a PIL image
        img = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw", 
            heif_file.mode
        )
        
        # Save as .jpg
        img.convert('RGB').save(output_path, 'JPEG')
        print(f"Converted: {file_name} -> {output_path}")

print("Conversion complete.")
