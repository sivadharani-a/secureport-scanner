from datetime import datetime

def build_report_dict(target: str, results: dict):
    open_ports = [p for p, status in results.items() if status == "open"]
    return {
        "target": target,
        "scanned_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "open_ports": open_ports,
        "raw_results": results,
        "summary": "Demo scan on common ports."
    }
