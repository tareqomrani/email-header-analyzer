
import re

def analyze_email_header(file_path):
    with open(file_path, 'r') as file:
        header = file.read()

    results = {}

    spf_match = re.search(r'SPF=(\w+)', header, re.IGNORECASE)
    results['SPF'] = spf_match.group(1) if spf_match else 'Not Found'

    dkim_match = re.search(r'DKIM=(\w+)', header, re.IGNORECASE)
    results['DKIM'] = dkim_match.group(1) if dkim_match else 'Not Found'

    dmarc_match = re.search(r'dmarc=\w+ \((\w+)', header, re.IGNORECASE)
    results['DMARC'] = dmarc_match.group(1) if dmarc_match else 'Not Found'

    from_match = re.search(r'From: .*@(\S+)', header)
    reply_to_match = re.search(r'Reply-To: .*@(\S+)', header)
    if from_match and reply_to_match:
        results['From vs Reply-To Mismatch'] = from_match.group(1) != reply_to_match.group(1)
    else:
        results['From vs Reply-To Mismatch'] = 'Not Enough Data'

    print("Header Analysis Results:")
    for k, v in results.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    analyze_email_header("sample_headers/phishy_header.txt")
