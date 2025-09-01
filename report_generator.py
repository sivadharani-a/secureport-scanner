from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(target, results=None):
    filename = f"{target}_scan_report.pdf"
    filepath = os.path.join(os.getcwd(), filename)

    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"SecurePort Scanner Report", styles["Title"]))
    elements.append(Paragraph(f"Target: {target}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    if results:
        data = [["Port", "Status"]]
        for r in results:
            data.append([r["port"], r["status"]])

        table = Table(data, colWidths=[100, 200])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
    else:
        elements.append(Paragraph("No results available.", styles["Normal"]))

    doc.build(elements)
    return filepath
