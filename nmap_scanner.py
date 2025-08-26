import subprocess

def run_nmap_scan(target):
    try:
        # -Pn skips ping (works on hosts blocking ICMP)
        result = subprocess.getoutput(f"nmap -Pn -T4 {target}")
        return result
    except Exception as e:
        return f"Error running Nmap scan: {str(e)}"
