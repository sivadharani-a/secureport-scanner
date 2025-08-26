from jinja2 import Template
import pdfkit

def generate_report(scan_data, template_file="templates/report.html", output_file="report.pdf"):
    with open(template_file) as f:
        template = Template(f.read())
    html_report = template.render(results=scan_data)
    pdfkit.from_string(html_report, output_file)
    return output_file
