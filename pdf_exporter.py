from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
from datetime import datetime


def add_watermark(c, text="SecurePort Scanner Security Labs"):
    """
    Adds a diagonal watermark to the current page.
    """
    c.saveState()
    c.setFont("Helvetica-Bold", 40)
    c.setFillGray(0.8, 0.3)  # light gray, transparent
    c.translate(300, 400)    # move center
    c.rotate(45)             # rotate diagonal
    c.drawCentredString(0, 0, text)
    c.restoreState()


class WatermarkDocTemplate(SimpleDocTemplate):
    def afterPage(self, c, doc):
        add_watermark(c)


def generate_pdf(target, nmap_results, socket_results, recommendations, brand_name="SecurePort Scanner Security Labs"):
    """
    Generate a PDF scan report with watermark.
    """
    filename = f"scan_report_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(os.getcwd(), filename)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Heading1", fontSize=16, spaceAfter=10, leading=20))
    styles.add(ParagraphStyle(name="BodyText", fontSize=12, leading=16))

    doc = WatermarkDocTemplate(filepath, pagesize=letter)
    story = []

    # Title
    story.append(Paragraph(f"Scan Report for {target}", styles["Heading1"]))
    story.append(Spacer(1, 12))

    # Nmap
    story.append(Paragraph("📄 Nmap Results", styles["Heading1"]))
    story.append(Paragraph(f"<pre>{nmap_results}</pre>", styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Socket
    story.append(Paragraph("📡 Socket Scan Results", styles["Heading1"]))
    story.append(Paragraph(f"{socket_results}", styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Recommendations
    story.append(Paragraph("🛡 Security Recommendations", styles["Heading1"]))
    for rec in recommendations:
        story.append(Paragraph(f"• {rec}", styles["BodyText"]))
    story.append(Spacer(1, 12))

    doc.build(story)

    return filepath
