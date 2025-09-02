import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template, request, redirect, url_for, send_file
from scanner.socket_scanner import run_socket_scan

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        target = request.form.get("target", "").strip()
        ports = request.form.get("ports", "20-1024").strip()
        results = run_socket_scan(target, ports)
        return render_template("results.html", target=target, results=results)
    return render_template("scan.html")


if __name__ == "__main__":
    app.run(debug=True)



