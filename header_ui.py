import re
import streamlit as st

st.title("Email Header Analyzer")
st.write("Paste a raw email header below to detect SPF, DKIM, DMARC results and spoofing risks.")

header_input = st.text_area("Email Header", height=300)

def analyze_email_header(header):
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

    return results

if st.button("Analyze"):
    if header_input.strip():
        results = analyze_email_header(header_input)
        st.subheader("Analysis Results")
        for key, value in results.items():
            st.write(f"**{key}:** {value}")
    else:
        st.warning("Please paste an email header to analyze.")