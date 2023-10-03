import face_recognition
import os

# Data Collection and Preprocessing (Organize your dataset)

# Face Detection (Not shown here, but you need to detect and crop faces)

# Face Recognition Model
known_face_encodings = []
known_face_names = []

# Training the Face Recognition Model
for folder_name in os.listdir("student_faces"):
    if os.path.isdir(os.path.join("student_faces", folder_name)):
        for filename in os.listdir(os.path.join("student_faces", folder_name)):
            image_path = os.path.join("student_faces", folder_name, filename)
            known_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(known_image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(folder_name)

# Save the trained model for later use
