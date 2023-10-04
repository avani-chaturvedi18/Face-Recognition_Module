import cv2
import dlib
from deepface import DeepFace
import numpy as np
import pandas as pd
import os
import csv
from datetime import datetime

def mark_attendance(attendance_csv, student_data, recognized_name):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(attendance_csv, mode='a', newline='') as file:
        writer = csv.writer(file)

        if recognized_name in student_data:
            writer.writerow([current_time, recognized_name, "Present"])
        else:
            writer.writerow([current_time, "Unknown", "Absent"])