from flask import Flask, request, jsonify
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

#  API Endpoint for Attendance Marking
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    # Implement code to receive the PDF file and process it for attendance marking
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    uploaded_file = request.files['file']
    
    if uploaded_file.filename == '':
        return jsonify({"error": "No selected file"})

    # Process the uploaded PDF file to extract student names and roll numbers
    student_info = extract_student_info(uploaded_file)

    # Implement face recognition logic to mark attendance
    # You need to match student_info with known student faces

    # Create a list of students with attendance status (present/absent)
    marked_attendance = []

    # Example: Mark attendance for each student
    for student in student_info:
        attendance_status = "Present"  # Modify based on your logic
        marked_attendance.append({"Name": student["Name"], "Roll Number": student["Roll Number"], "Status": attendance_status})

    # Generating the Marked Attendance PDF
    marked_attendance_pdf = generate_attendance_pdf(marked_attendance)

    return jsonify({"result": "Attendance marked successfully", "pdf_path": marked_attendance_pdf})

# Function to extract student info from the uploaded PDF
def extract_student_info(pdf_file):
    student_info = []
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Implement code to extract student names and roll numbers here
    # Populate student_info with the extracted data
    return student_info

# Function to generate the marked attendance PDF
def generate_attendance_pdf(marked_attendance):
    marked_attendance_pdf = "marked_attendance.pdf"
    c = canvas.Canvas(marked_attendance_pdf, pagesize=letter)
    c.drawString(100, 750, "Attendance Report")

    # Add attendance information to the PDF
    y_coordinate = 700
    for student in marked_attendance:
        name = student["Name"]
        roll_number = student["Roll Number"]
        status = student["Status"]
        c.drawString(100, y_coordinate, f"Name: {name}, Roll Number: {roll_number}, Status: {status}")
        y_coordinate -= 20

    c.save()
    return marked_attendance_pdf

# API Endpoint for Downloading the Marked Attendance PDF
@app.route('/download_attendance', methods=['GET'])
def download_attendance():
    # Implement code to allow users to download the marked attendance PDF
    pdf_path = "marked_attendance.pdf"  # Change to the actual path of the generated PDF
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
