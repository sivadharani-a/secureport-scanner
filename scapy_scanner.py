import socket

def run_scapy_scan(target, ports=[22, 80, 443, 8080, 3306]):
    open_ports = []
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        return f"Open Ports: {', '.join(map(str, open_ports))}" if open_ports else "No open ports detected"
    except Exception as e:
        return f"Error during scan: {str(e)}"
