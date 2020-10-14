import sys
import requests

def inspectResponseHeader(headers, expectedHeader, expectedValue):
    actualValue = ""

    try:
        actualValue = headers[expectedHeader]
    except:
        print("[Alert] header {} not found".format(expectedHeader))
        return

    if actualValue == expectedValue:
        print("[Success] {} configured correctly".format(expectedHeader))
    else:
        print("[Alert] {} configured incorrectly".format(expectedHeader))
        print("  Expected: '{}' but found '{}'".format(expectedValue, actualValue))


def fetchResponseHeaders(targetUrl):
    print("Fetching headers of {}".format(targetUrl))
    response = requests.get(targetUrl)
    print("{} {}".format(response.status_code, response.reason))
    return response.headers

xssProtectionHeader = "X-XSS-Protection"
xssProtectionHeaderValue = "1; mode=block"
xFrameOptionsHeader = "X-Frame-Options"
xFrameOptionsHeaderValue = "DENY"
xContentTypeOptionsHeader = "X-Content-Type-Options"
xContentTypeOptionsHeaderValue = "nosniff"

if len(sys.argv) < 2:
    print("Usage: python {} <target url>".format(sys.argv[0]))
    sys.exit()

targetUrl = sys.argv[1]
headers = fetchResponseHeaders(targetUrl)

inspectResponseHeader(headers, xssProtectionHeader, xssProtectionHeaderValue)
inspectResponseHeader(headers, xFrameOptionsHeader, xFrameOptionsHeaderValue)
inspectResponseHeader(headers, xContentTypeOptionsHeader, xContentTypeOptionsHeaderValue)
inspectResponseHeader(headers, "h1", "sdf")
inspectResponseHeader(headers, "Content-Type", "mocked expected value")

