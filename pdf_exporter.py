import os
import tempfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_report_pdf(report: dict) -> str:
    fd, path = tempfile.mkstemp(prefix="scan_report_", suffix=".pdf")
    os.close(fd)

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "SecurePort Scanner — Report")
    y -= 25

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Target: {report.get('target')}")
    y -= 18
    c.drawString(50, y, f"Scanned At: {report.get('scanned_at')}")
    y -= 18
    c.drawString(50, y, f"Summary: {report.get('summary')}")
    y -= 24

    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Open Ports")
    y -= 18

    c.setFont("Helvetica", 12)
    open_ports = report.get("open_ports") or []
    if open_ports:
        for p in open_ports:
            c.drawString(60, y, f"- {p}")
            y -= 16
    else:
        c.drawString(60, y, "None detected")
        y -= 16

    c.showPage()
    c.save()
    return path
