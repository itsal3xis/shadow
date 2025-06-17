import requests

def run(url):
    print("[Fingerprinting] Running...")
    try:
        r = requests.get(url, timeout=3)
        if "WordPress" in r.text:
            print("[+] WordPress detected")
        if "X-Powered-By" in r.headers:
            print(f"[+] X-Powered-By: {r.headers['X-Powered-By']}")
        if "Server" in r.headers:
            print(f"[+] Server: {r.headers['Server']}")
    except:
        print("[!] Failed to fingerprint target")