import socket

def run_socket_scan(target: str, ports=None, timeout=1.0):
    """
    Returns a dict: { port_number: "open"/"closed"/"error:<msg>" }
    Keep it lightweight for PaaS (no massive port ranges).
    """
    results = {}
    if not target:
        return results
    if ports is None:
        ports = [22, 80, 443]

    for port in ports:
        try:
            with socket.create_connection((target, port), timeout=timeout):
                results[port] = "open"
        except socket.timeout:
            results[port] = "closed"
        except Exception as e:
            # Many PaaS will block raw TCP; you may see errors or false-closed.
            results[port] = f"error:{type(e).__name__}"

    return results
