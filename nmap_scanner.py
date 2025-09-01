import nmap

def run_nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, "20-1024")
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]["state"]
                results.append({"port": port, "status": state})
    if not results:
        results.append({"port": "-", "status": "No open ports detected"})
    return results
