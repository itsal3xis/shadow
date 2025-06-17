import requests

def lookup_cves(product, version):
    print(f"[CVE Lookup] Searching CVEs for {product} {version}...")

    try:
        # Format product for query, remove spaces etc
        product_clean = product.lower().replace(' ', '')
        url = f"https://cve.circl.lu/api/search/{product_clean}/{version}"

        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("[!] CVE API request failed")
            return []

        data = response.json()
        cves = data.get('results', [])
        if not cves:
            print("[CVE Lookup] No CVEs found")
            return []

        for cve in cves[:5]:  # limit to top 5 results
            print(f" - {cve.get('id')}: {cve.get('summary')[:100]}...")
            print(f"   Link: https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve.get('id')}")
        return cves

    except Exception as e:
        print(f"[!] Error during CVE lookup: {e}")
        return []
