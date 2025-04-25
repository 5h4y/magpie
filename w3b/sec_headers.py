import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy",
    "Expect-CT",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Resource-Policy",
]

def check_security_headers(domain):
    if not domain.startswith("http"):
        domain = "https://" + domain

    try:
        response = requests.get(domain, timeout=5)
        headers = response.headers

        print(f"\n🔎 Security headers for {domain}:\n")

        for h in SECURITY_HEADERS:
            val = headers.get(h)
            if val:
                print(f"✅ {h}: {val}")
            else:
                print(f"⚠️  {h} not present")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Could not reach {domain}\n{e}")

check_security_headers(input())

# future ideas: flag weak values, add batch mode, output to md, json, csv, etc.
