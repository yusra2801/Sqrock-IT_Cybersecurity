### Day 25 — File Upload Vulnerability & Magic Bytes Validator

Attackers often bypass file-extension checks by renaming executable scripts (e.g. `.php`) to look like harmless files (e.g. `.jpg`). Checking the actual binary header (magic bytes) instead of trusting the file extension confirms whether the content genuinely matches the claimed format. In this task, I built a validator that reads the first bytes of a file and compares them against known signatures for PNG and JPEG. I tested it against two files: a genuine PNG (correct magic bytes) and a file disguised as a `.jpg` that actually contained PHP code. The validator correctly passed the real PNG and flagged the fake `.jpg` as an invalid signature — exactly the kind of malicious upload attempt this check is meant to catch.

**Secure file upload practices:**
- Always validate magic bytes server-side — never trust the file extension or the client-supplied MIME type
- Store uploaded files outside the web-served directory, or with randomized names, so even a successfully uploaded malicious file can't be directly executed via a URL
- Re-encode/re-process uploaded images (e.g. resize) rather than storing the raw upload, which strips out any embedded malicious payload