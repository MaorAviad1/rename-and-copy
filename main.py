import os
import shutil
import re

def extract_sku(filename):
    match = re.match(r"^(m[0-9]+d)_", filename)
    return match.group(1) if match else None

src_folder = "D:\\Stores\\strs"
dest_folder = "D:\\allimagessku"

for root, dirs, files in os.walk(src_folder):
    for file in files:
        if file.endswith('.png'):
            sku = extract_sku(file)
            if sku is not None:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, sku + '.png')
                shutil.copy2(src_file_path, dest_file_path)
