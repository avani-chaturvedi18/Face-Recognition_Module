from flask import Flask, request, render_template, redirect, url_for
import os
import face_recognition

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the uploaded image
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Perform face recognition on the uploaded image
        # Implement face recognition logic here using face_recognition library
def face_recognition():
    # Load known face encodings and names from your database or file
    known_face_encodings = [...]  # List of known face encodings
    known_face_names = [...]      # List of corresponding names

    # Load the uploaded image for face recognition
    uploaded_image_path = "path_to_uploaded_image.jpg"
    uploaded_image = face_recognition.load_image_file(uploaded_image_path)

    # Find face locations and encodings in the uploaded image
    face_locations = face_recognition.face_locations(uploaded_image)
    face_encodings = face_recognition.face_encodings(uploaded_image, face_locations)

    recognized_faces = []

    # Compare face encodings in the uploaded image to known faces
    for face_encoding in face_encodings:
        # Compare this face encoding to the list of known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name for unrecognized faces

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        return recognized_faces.append(name)

    # Return the result (recognized faces) as a list
    recognized_faces

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
