import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389, 3306, 8080]

def run_socket_scan(target, ports=None):
    if ports is None:
        ports = COMMON_PORTS

    results = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            sock.connect((target, port))
            results.append({"port": port, "status": "Open"})
        except:
            pass
        finally:
            sock.close()

    if not results:
        results.append({"port": "-", "status": "No open ports detected"})
    return results
