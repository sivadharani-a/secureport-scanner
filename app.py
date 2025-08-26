from flask import Flask, render_template, request, send_file
import subprocess
import socket
from pdf_exporter import generate_pdf
import os
from datetime import datetime

app = Flask(__name__)

# Function to run Nmap scan
def run_nmap_scan(target):
    try:
        result = subprocess.getoutput(f"nmap -sS -Pn {target}")
        return result
    except Exception as e:
        return str(e)

# Function for socket-based quick scan
def run_socket_scan(target, ports=[22, 80, 443, 3306, 8080]):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports

# Function to generate simple recommendations
def generate_recommendations(open_ports):
    recs = []
    if 22 in open_ports:
        recs.append("SSH detected → Use key-based auth, disable root login, change default port.")
    if 80 in open_ports:
        recs.append("HTTP detected → Enforce HTTPS with TLS.")
    if 443 in open_ports:
        recs.append("HTTPS detected → Ensure TLS version >= 1.2, use strong ciphers.")
    if not recs:
        recs.append("No critical issues detected. Maintain patching and monitoring.")
    return "\n".join(recs)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form["target"]

        nmap_results = run_nmap_scan(target)
        socket_results = run_socket_scan(target)
        socket_str = ", ".join(map(str, socket_results)) if socket_results else "No open ports detected"

        recommendations = generate_recommendations(socket_results)

        return render_template(
            "results.html",
            target=target,
            nmap_results=nmap_results,
            socket_results=socket_str,
            recommendations=recommendations
        )
    return render_template("index.html")

@app.route("/export", methods=["POST"])
def export_pdf():
    target = request.form.get("target")
    nmap_results = request.form.get("nmap_results")
    socket_results = request.form.get("socket_results")
    recommendations = request.form.getlist("recommendations")

    filepath = generate_pdf(
        target=target,
        nmap_results=nmap_results,
        socket_results=socket_results,
        recommendations=recommendations,
        brand_name="SecurePort Scanner Security Labs"
    )
    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
