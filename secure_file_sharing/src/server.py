# src/server.py
import socket
from src.config import HOST, PORT, MAX_CONNECTIONS
from src.utils.logger import logger

# Import our new HTTP classes!
from src.http.request import HTTPRequest
from src.http.response import build_response

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    logger.info(f"Server is now listening on {HOST}:{PORT}")

    try:
        while True:
            logger.info("Waiting for a client to connect...")
            client_socket, client_address = server_socket.accept()
            logger.info(f"Connection established with {client_address}")

            try:
                # 5a. Receive data
                data = client_socket.recv(1024)
                if not data:
                    continue # If browser sent nothing, skip to the next loop

                # Parse the raw bytes into our HTTPRequest object
                request = HTTPRequest(data)

                if request.path == "/":
                    body_text = "Welcome to the File Server"
                    response_bytes = build_response(body_text, 200, "OK")
                    
                elif request.path == "/secret":
                    body_text = "This is a secret area"
                    response_bytes = build_response(body_text, 200, "OK")
                    
                else:
                    body_text = "404 - Page Not Found"
                    response_bytes = build_response(body_text, 404, "Not Found")
                # ==========================================

                # 5b. Send the properly formatted HTTP response back
                client_socket.sendall(response_bytes)

            except Exception as e:
                logger.error(f"Error handling client: {e}", exc_info=True)
            finally:
                # 6. Close the client connection
                client_socket.close()
                logger.info("Client connection closed.")

    except KeyboardInterrupt:
        logger.info("Server manually stopped.")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
    finally:
        # Shut down the main server socket
        server_socket.close()
        logger.info("Server socket closed.")