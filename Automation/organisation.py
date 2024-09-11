import os
import shutil
from time import sleep

# Define source (Downloads folder) and destination folders
source_folder = '/Users/your_username/Downloads/'
destination_folders = {
    '.pdf': '/Users/your_username/Documents/PDFs',
    '.jpg': '/Users/your_username/Pictures',
    '.mp4': '/Users/your_username/Videos',
}

def organize_downloads():
    while True:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                if file_extension in destination_folders:
                    shutil.move(file_path, destination_folders[file_extension])
                    print(f"Moved {filename} to {destination_folders[file_extension]}")
        sleep(3600)  # Run every hour

organize_downloads()
