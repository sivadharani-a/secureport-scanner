from scapy.all import sr1, IP, TCP

def run_scapy_scan(target, ports=None):
    if ports is None:
        ports = range(20, 1025)

    results = []
    for port in ports:
        pkt = IP(dst=target)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=0.5, verbose=0)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
            results.append({"port": port, "status": "Open"})
    if not results:
        results.append({"port": "-", "status": "No open ports detected"})
    return results
