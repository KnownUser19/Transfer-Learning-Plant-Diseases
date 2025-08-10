import zipfile
import os


def unzip_dataset(zip_file_path, extraction_path):
    if not os.path.exists(extraction_path):
        os.makedirs(extraction_path)

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)

    print(f"Dataset successfully extracted to {extraction_path}")


zip_file_path = 'D:\Plant_Disease_Classification\Data\plant_village.zip' # paste address of path of zip file
extraction_path = 'D:\Plant_Disease_Classification\Data\plant_village'   # paste address of path where you want to place your zip file

unzip_dataset(zip_file_path, extraction_path)
