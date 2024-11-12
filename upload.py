import os
import boto3
import shutil
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'mgg-so-ueia-2024'  

local_directory = './stored_files'  

# Function to upload files to S3
def upload_to_s3(file_path):
    file_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"Uploaded {file_name} to S3 bucket {bucket_name}")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")

# Function to delete local JSON files
def delete_local_files():
    for filename in os.listdir(local_directory):
        if filename.endswith(".json"):
            file_path = os.path.join(local_directory, filename)
            upload_to_s3(file_path)
            os.remove(file_path)
            print(f"Deleted {file_path}")

if __name__ == "__main__":
    delete_local_files()
