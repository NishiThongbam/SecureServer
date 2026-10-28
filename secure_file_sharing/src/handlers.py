from src.http.request import HTTPRequest
from src.http.response import build_response

def handle_home(request: HTTPRequest)-> bytes:
    return build_response("Welcome to the Secure File Server Touter")

def handle_secret(request: HTTPRequest)-> bytes:
    return build_response("YOu found the secret area.")


def handle_upload_stub(request: HTTPRequest)-> bytes:
    if request.method =="POST":
        return build_response("File Uploaded successfully")
    return build_response("Please POST a file to this endpoint.", 400, "Bad Request")

def handle_about(request:HTTPRequest):
    return build_response("ABout this MCA MINI Project")

