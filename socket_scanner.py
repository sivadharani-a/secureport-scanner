import socket

def run_socket_scan(target: str, ports: str = "20-1024"):
    opened = []
    if "-" in ports:
        start, end = [int(x) for x in ports.split("-", 1)]
        port_list = range(start, end + 1)
    else:
        port_list = [int(p) for p in ports.split(",") if p.strip().isdigit()]

    for p in port_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            if s.connect_ex((target, p)) == 0:
                opened.append((p, "open"))
        finally:
            s.close()
    return opened
