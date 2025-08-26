# db.py
import sqlite3
from datetime import datetime

DB_NAME = "scan_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            nmap_results TEXT,
            socket_results TEXT,
            recommendations TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_scan(target, nmap_results, socket_results, recommendations):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scans (target, nmap_results, socket_results, recommendations)
        VALUES (?, ?, ?, ?)
    ''', (target, nmap_results, socket_results, recommendations))
    conn.commit()
    conn.close()

def get_scans():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, target, timestamp FROM scans ORDER BY timestamp DESC")
    scans = cursor.fetchall()
    conn.close()
    return scans

def get_scan_by_id(scan_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans WHERE id=?", (scan_id,))
    scan = cursor.fetchone()
    conn.close()
    return scan
