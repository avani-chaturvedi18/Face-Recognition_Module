import cv2
#import dlib
#from deepface import DeepFace
import numpy as np
import pandas as pd
import os
import csv
from datetime import datetime

def extract_data(excel_filename, image_dir):
    extracted_data = []

    try:
        df = pd.read_excel(excel_filename)

        for index, row in df.iterrows():
            name = row["name"]
            roll_no = row["roll_number"]
            image_path = row["image_path"]

            if os.path.exists(image_path):
                extracted_data.append({"name": name, "roll_number": roll_no, "image_path": image_path})

    except Exception as e:
        print("Error extracting data from excel:", e)

    return extracted_data
