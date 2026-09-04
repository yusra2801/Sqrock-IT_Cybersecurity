


import html
import re


def sanitize_user_input(raw_payload):
    # Step 1: encode special characters (< becomes &lt;, etc.)
    encoded_string = html.escape(raw_payload)
    # Step 2: strip out dangerous keywords even after encoding
    stripped_output = re.sub(r"(?i)script|onerror|onload", "[PROHIBITED_TOKEN]", encoded_string)
    return stripped_output


if __name__ == "__main__":
    test_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "<body onload=alert('hacked')>",
        "<b>Hello world</b>",
        "<a href='javascript:alert(1)'>click</a>",
        "normal comment, no attack here",
        "<script src='http://evil.com/steal.js'></script>",
        "<svg onload=alert(1)>",
        "<iframe src='javascript:alert(1)'></iframe>",
        "<div onclick=alert(1)>click me</div>",
    ]

    for payload in test_payloads:
        print(f"Raw Input: {payload}")
        print(f"Sanitized: {sanitize_user_input(payload)}\n")