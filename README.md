🔒 SecurePort Scanner Security Labs

A simple yet powerful network security scanner that detects open ports on a target host using both Nmap and a custom Python socket scanner.
It also provides basic security recommendations and allows exporting scan reports as PDF for documentation.

✨ Features

✅ Dual scanning engine → Nmap + Python socket scan

✅ Detects open & filtered ports

✅ Provides security best-practice tips

✅ Export scan results as PDF reports

✅ Modern Flask web interface with improved UI/UX

📦 Tech Stack

Backend: Python (Flask, Socket, Subprocess)

Scanning Tools: Nmap, Custom Socket Scanner

PDF Reports: ReportLab

Frontend: HTML, CSS (Bootstrap/Tailwind mix)

🚀 Setup & Usage
1️⃣ Clone the Repository
git clone https://github.com/sivadharani-a/secureport-scanner.git
cd secureport-scanner

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv

# Activate the venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

3️⃣ Run the App
python app.py

4️⃣ Access in Browser

👉 Open: http://127.0.0.1:5000

📂 Project Structure
secureport-scanner/
│── app.py               # Main Flask app
│── pdf_exporter.py      # PDF generation logic
│── scanner/             # Scanning logic (Nmap + Socket)
│── templates/           # HTML templates (UI)
│── static/              # CSS, JS, assets
│── requirements.txt     # Python dependencies
│── README.md            # Documentation

📥 Exporting Scan Reports

->After completing a scan, click "Export as PDF" to download a professional report containing:

->Host information

->Open ports detected

->Security recommendations

🛡 Future Enhancements

🌐 Live network device discovery

📊 Interactive dashboards with graphs

🔔 Email alerts for vulnerable services

🖥 Dark mode UI support

☁ Deployment on cloud (Heroku / Netlify + Backend API)

🔐 Disclaimer

This project is for educational & ethical use only. Do not scan systems without proper authorization.
