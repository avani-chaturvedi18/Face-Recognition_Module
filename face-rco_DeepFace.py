from mark_attendance import mark_attendance
from excelevent import extract_data
# Load the data from Excel
excel_filename = "your_excel_file.xlsx"
image_dir = "your_image_directory"
data = extract_data(excel_filename, image_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load a pre-trained dlib face detector
detector = dlib.get_frontal_face_detector()

# List of available DeepFace models
available_models = ["Facenet", "VGG-Face", "OpenFace", "DeepFace", "DeepID", "Dlib"]

# CSV file to record attendance
attendance_csv = "attendance.csv"

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame using dlib
    faces = detector(gray)

    for face in faces:
        # Extract the coordinates of the detected face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Crop the face from the frame
        face_img = frame[y:y+h, x:x+w]

        # Resize the face image for DeepFace input (160x160)
        face_img = cv2.resize(face_img, (160, 160))

        for model_name in available_models:
            try:
                # Perform face recognition using the current model
                recognized_name = "Unknown"  # Initialize as "Unknown"

                for entry in data:
                    if DeepFace.verify(face_img, image_path=entry["image_path"], model_name=model_name)["verified"]:
                        recognized_name = entry["name"]
                        break  # Stop searching after a match is found

                # Display the recognized name on the frame
                cv2.putText(frame, f"Model: {model_name}, Name: {recognized_name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Mark attendance in the CSV file
                mark_attendance(attendance_csv, [entry["name"] for entry in data], recognized_name)

            except Exception as e:
                print(f"Error with model {model_name}: {e}")

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