import socket

def socket_scan(target, ports=[22, 80, 443, 8080, 3306]):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)   # keep as integer
            sock.close()
        except Exception:
            pass
    return open_ports
