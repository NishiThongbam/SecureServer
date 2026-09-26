from src.utils.logger import logger

class HTTPRequest:
    def __init__(self, raw_data:bytes):
        self.method= ""
        self.path= ""
        self.version= ""
        self.headers= {}


        #Decode the raw bytes into a string
        request_text = raw_data.decode('utf-8', errors='replace')
        self._parse(request_text)

    def _parse(self, request_text:str):
        #HTTP lines are separated by \r\n
        lines = request_text.split('\r\n')


        if not lines or not lines[0]:
            return


        #Parse the Request Line 
        request_line = lines[0].split(' ')
        if len(request_line)==3:
            self.method = request_line[0]
            self.path = request_line[1]
            self.version = request_line[2]
            logger.debug(f"Parsed Request: {self.method} {self.path}")
