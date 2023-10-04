from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_attendance_pdf(name, roll_number):
    # Create a PDF file
    pdf_filename = f"{name}_{roll_number}_attendance.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Add text fields for name and roll number
    c.drawString(100, 700, f"Name: {name}")
    c.drawString(100, 680, f"Roll Number: {roll_number}")

    # Add attendance marking section
    c.drawString(100, 640, "Attendance:")
    # Implement attendance marking logic here

    # Save the PDF file
    c.save()

    return pdf_filename
