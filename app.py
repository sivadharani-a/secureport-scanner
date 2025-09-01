from flask import Flask, render_template, request, send_file, session
from scanner.socket_scanner import run_socket_scan
from scanner.nmap_scanner import run_nmap_scan
from scanner.scapy_scanner import run_scapy_scan
from pdf_exporter import generate_pdf
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session storage

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        target = request.form["target"]
        method = request.form.get("method", "socket")
        results = []

        if method == "socket":
            results = run_socket_scan(target)
        elif method == "nmap":
            results = run_nmap_scan(target)
        elif method == "scapy":
            results = run_scapy_scan(target)

        # Save results in session for PDF download
        session["last_scan"] = {"target": target, "results": results}

        return render_template("results.html", target=target, results=results)

    return render_template("scan.html")

@app.route("/download")
def download_report():
    scan_data = session.get("last_scan")
    if not scan_data:
        return "No scan data available.", 400

    filepath = generate_pdf(scan_data["target"], scan_data["results"])
    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
