import sys, requests, json;
from requests.exceptions import HTTPError;

try:
    license_request = json.load(sys.stdin)
except Exception as err:
    exit(1)

try:
    minisap_url = "https://go.support.sap.com/minisap/odata/bkey/minisap/"
    minisap_headers = {
        "x-csrf-token": "Fetch",
        "Connection": "keep-alive"
    }    
    session = requests.Session()
    response = session.get(minisap_url, headers = minisap_headers )
except HTTPError as http_err:
    print(response.text, file=sys.stderr)
    exit(-1)
except Exception as err:
    exit(2) 

try:
    minisap_post_url = minisap_url + "/LicenseKey"
    minisap_post_headers = {
        "x-csrf-token": response.headers.get("x-csrf-token"),
        "Connection": "keep-alive",
        "Content-Type": "application/json"
    }    
    minisap_post_response = session.post(minisap_post_url, headers = minisap_post_headers, data=json.dumps(license_request))
    minisap_post_response.raise_for_status()
except HTTPError as http_err:
    print(minisap_post_response.text, file=sys.stderr)
    exit(-1)
except Exception as err:
    exit(3)

print(minisap_post_response.text)
exit(0)
