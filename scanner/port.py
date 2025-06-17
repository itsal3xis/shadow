import nmap
import shutil
from scanner import cve_lookup

def run(host):
    print("[Port + Service Scan] Running with Nmap...")
    if shutil.which("nmap") is None:
        print("[!] Nmap is not installed or not in PATH")
        return

    nm = nmap.PortScanner()
    try:
        nm.scan(host, arguments="-p- -sV")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                service = nm[host][proto][port]
                name = service.get('name', 'unknown')
                product = service.get('product', '')
                version = service.get('version', '')

                line = f"[+] Port {port}/tcp | {name} | {product} {version}".strip()
                print(line)

                # Lookup CVEs if product and version available
                if product and version:
                    cve_lookup.lookup_cves(product, version)

    except Exception as e:
        print(f"[!] Nmap error: {e}")
