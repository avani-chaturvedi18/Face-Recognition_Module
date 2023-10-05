import cv2
from deepface import DeepFace
from mark_attendance import mark_attendance
from excelevent import extract_data

# Load the data from Excel
excel_filename = "your_excel_file.xlsx"
image_dir = "image_directory"
data = extract_data(excel_filename, image_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load the Haar Cascade classifier for face detection (you might need to provide the path to the XML file)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# CSV file to record attendance
attendance_csv = "attendance.csv"

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame using Haar Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Crop the face from the frame
        face_img = frame[y:y+h, x:x+w]

        # Resize the face image for DeepFace input (152x152, required by DeepID)
        face_img = cv2.resize(face_img, (152, 152))

        try:
            # Perform face recognition using the DeepID model
            recognized_name = "Unknown"  # Initialize as "Unknown"

            for entry in data:
                result = DeepFace.verify(face_img, image_path=entry["image_path"], model_name="DeepID")
                if result["verified"]:
                    recognized_name = entry["name"]
                    break  # Stop searching after a match is found

            # Display the recognized name on the frame
            cv2.putText(frame, f"Model: DeepID, Name: {recognized_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Mark attendance in the CSV file
            mark_attendance(attendance_csv, [entry["name"] for entry in data], recognized_name)

        except Exception as e:
            print(f"Error: {e}")

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with face recognition results
    cv2.imshow("Face Recognition", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
