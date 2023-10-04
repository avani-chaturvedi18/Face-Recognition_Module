from flask import send_file

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    # Face recognition and verification logic
    name = 'John Doe'  # Replace with the recognized name
    roll_number = '12345'  # Replace with the recognized roll number

    # Generate the attendance PDF
    pdf_filename = generate_attendance_pdf(name, roll_number)

    # Return the PDF file as a response
    return send_file(pdf_filename, as_attachment=True)
