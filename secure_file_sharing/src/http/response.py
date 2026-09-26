# src/http/response.py
def build_response(body: str, status_code: int = 200, status_text: str = "OK") -> bytes:
    response_line = f"HTTP/1.1 {status_code} {status_text}\r\n"
    content_type = "Content-Type: text/plain\r\n"
    
    body_bytes = body.encode('utf-8')
    content_length = f"Content-Length: {len(body_bytes)}\r\n"
    
    # CRITICAL: There must be an extra \r\n here to create the blank line!
    headers = response_line + content_type + content_length + "\r\n"
    
    return headers.encode('utf-8') + body_bytes