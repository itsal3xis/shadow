import argparse
from scanner import port, xss, sqli, dirbust, fingerprint, lfi, rce, cve



def main():
    parser = argparse.ArgumentParser(description="SHADOW - Stealthy Hacker's Automated Discovery Of Weaknesses")
    parser.add_argument("--target", required=True, help="Target URL or IP")
    parser.add_argument("--scan", default="all", help="Comma-separated list: port,xss,sqli,dir,fingerprint")
    parser.add_argument("--wordlist", help="Path to wordlist for directory brute-forcing")
    args = parser.parse_args()

    target = args.target.rstrip('/')
    scans = args.scan.split(',')

    print(f"[VulnReaper] Scanning: {target}\n")

    if "port" in scans or "all" in scans:
        port.run(target)
    if "xss" in scans or "all" in scans:
        xss.run(target)
    if "sqli" in scans or "all" in scans:
        sqli.run(target)
    if "dir" in scans or "all" in scans:
        dirbust.run(target, wordlist=args.wordlist)
    if "fingerprint" in scans or "all" in scans:
        fingerprint.run(target)
    if "lfi" in scans or "all" in scans:
        lfi.run(target)
    if "rce" in scans or "all" in scans:
        rce.run(target)


if __name__ == "__main__":
    main()