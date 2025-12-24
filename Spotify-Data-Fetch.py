# This program helps to download dataset from Kaggle.com

import kagglehub
import shutil
import os

file_path = kagglehub.dataset_download(
    "wardabilal/spotify-global-music-dataset-20092025"
)
print(file_path)
source_path = f"{file_path}\Spotify_data clean.csv"
destination_path = r"C:\Users\HP\OneDrive\Desktop\Data Science\Spotify-Analysis"

if os.path.isfile(source_path) :
    shutil.move(source_path, destination_path)
    print("File moved successfully")
else:
    print("It doesn't exist.")
