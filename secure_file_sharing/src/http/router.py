from src.http.request import HTTPRequest
from src.http.response import build_response
from src.utils.logger import logger

class Router:
    def __init__(self):
        self.routes={}


    def add_route(self, method: str, path:str, handler_func):
        """Registers a new route"""
        self.routes[(method,path)]= handler_func
        logger.debug(f"Route added: {method} {path}")


    def handle_request(self, request: HTTPRequest)->bytes:
        """Finds the matching route"""
        #create a key from the incoming requests
        route_key=(request.method, request.path)

        # Look up the handler function in our dictionary
        handler = self.routes.get(route_key)


        if handler:
            # If we found a matching fucntion
            return handler(request)
        else:
            logger.warning(f"404 Not Found: {request.method} {request.path}")
            return build_response("404 - Page not found", 404, "NOT found")