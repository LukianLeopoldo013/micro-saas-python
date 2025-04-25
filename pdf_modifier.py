from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.colors import orange
from reportlab.lib.pagesizes import A4
from io import BytesIO
import os

def modify_pdf(filename, cpf, position, color, upload_folder):
    packet = BytesIO()
    canv = canvas.Canvas(packet, pagesize=A4)

    if position == 'top-left':
        x = 50
        y = 800
    elif position == 'top-right':
        x = 500
        y = 800
    elif position == 'bottom-left':
        x = 50
        y = 50
    elif position == 'bottom-right':
        x = 500
        y = 50
    else:
        raise ValueError("Invalid position")
    
    print( f"Draw of cpf in position: {x}, {y}")

    canv.setFillColor(color)
    canv.setFont("Helvetica", 12)
    canv.drawString(x, y, cpf)
    canv.save()

    try:
        packet.seek(0)
        new_pdf = PdfReader(packet)
        print("PDF created successfully")

    except Exception as e:
        print(f"Error creating PDF: {str(e)}")
      
    try:
        existing_pdf = PdfReader(open(os.path.join(upload_folder, filename), "rb"))
        print("PDF success open")
        output = PdfWriter()
        print(f"Number of pages is:  {len(existing_pdf.pages)}")
        for i in range(len(existing_pdf.pages)):
            page = existing_pdf.pages[i]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)
        with open(os.path.join(upload_folder, filename), "wb") as outputStream:
            output.write(outputStream)
        
        print(f"PDF modificado em: {os.path.join(upload_folder, filename)}")
    except Exception as e:
        print(f"Error to open the PDF: {str(e)}")

        
