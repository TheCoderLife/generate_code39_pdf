from barcode import Code39
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
import datetime


def generate_svg(web_input) -> str:
    code39 = Code39(web_input, add_checksum=False)  # checksum is cutting the last digit
    code39.save('lieferscheincode')
    return 'SVG File created successfully'


def generate_code39_pdf() -> str:
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # generate timestamp

    final_pdf = canvas.Canvas('generated_pdfs/'+timestamp + '.pdf')
    drawing = svg2rlg("lieferscheincode.svg")
    renderPDF.draw(drawing, final_pdf, 220, 400)
    final_pdf.save()

    return timestamp
