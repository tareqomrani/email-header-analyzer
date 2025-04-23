
# Email Header Analyzer

Scans raw email headers and flags SPF/DKIM/DMARC failures and suspicious 'From/Reply-To' mismatches.

## How to Run
```
python header_analyzer.py
```

## Features
- Identifies spoofing risks
- Basic phishing indicator logic
- Try the Streamlit interface by running: streamlit run header_ui.py
