import os
from flask import Flask, render_template, request, jsonify, send_file, url_for, redirect
from scanner.socket_scanner import run_socket_scan
from report_generator import build_report_dict
from pdf_exporter import export_report_pdf

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        target = (request.form.get("target") or "").strip()
        # Optional: limit to a few ports so most PaaS will allow it
        ports_raw = (request.form.get("ports") or "22,80,443").strip()
        try:
            ports = [int(p) for p in ports_raw.split(",") if p.strip().isdigit()]
        except Exception:
            ports = [22, 80, 443]

        results = run_socket_scan(target, ports=ports, timeout=1.0)
        return render_template("results.html", target=target, results=results)

    return render_template("scan.html")

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    target = request.form.get("target") or "unknown"
    # Expect results serialized in hidden field (JSON) or rebuild a minimal report
    # For simplicity, rebuild from quick re-scan of a few ports:
    results = run_socket_scan(target, ports=[22, 80, 443], timeout=1.0)
    report = build_report_dict(target, results)
    pdf_path = export_report_pdf(report)  # returns path to a temp PDF file
    return send_file(pdf_path, as_attachment=True, download_name=f"scan_report_{target}.pdf")

if __name__ == "__main__":
    # Local dev only. In Deta Space we’ll run via gunicorn.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
