import requests
from concurrent.futures import ThreadPoolExecutor

def check_path(url, path):
    full_url = f"{url.rstrip('/')}/{path}"
    try:
        r = requests.get(full_url, timeout=3)
        if r.status_code in [200, 403]:
            print(f"[FOUND] {full_url} ({r.status_code})")
    except:
        pass

def run(url, wordlist=None):
    print("[DirBuster] Running...")

    paths = ["admin", "login", "dashboard", ".git", "backup", ".env"]

    if wordlist:
        try:
            with open(wordlist, "r") as f:
                paths = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[!] Could not read wordlist: {e}")
            return

    with ThreadPoolExecutor(max_workers=20) as executor:
        for path in paths:
            executor.submit(check_path, url, path)
