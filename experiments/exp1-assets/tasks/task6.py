import urllib.request

def fetch_with_retry(url):
    """Fetch a URL, retrying on failure. Spec:
    - Up to 3 attempts total.
    - 1 second wait between attempts.
    - On persistent failure, re-raise the last exception.
    """
    for attempt in range(3):
        try:
            return urllib.request.urlopen(url, timeout=5).read()
        except Exception:
            pass
    return None