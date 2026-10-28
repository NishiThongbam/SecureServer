# src/server.py
import socket
from src.config import HOST, PORT, MAX_CONNECTIONS
from src.utils.logger import logger

# Import our new HTTP classes!
from src.http.request import HTTPRequest
from src.http.router import Router
from src.handlers import handle_home,handle_secret,handle_upload_stub, handle_about


def start_server():


    router=Router()
    router.add_route("GET","/", handle_home)
    router.add_route("GET", "/secret", handle_secret)
    router.add_route("POST","/upload", handle_upload_stub)
    router.add_route("GET","/about", handle_about)





    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    server_socket.settimeout(1.0)
    logger.info(f"Server is now listening on {HOST}:{PORT}")

    try:
        logger.info("Waiting for a client to connect...")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                
            except socket.timeout:
                continue

            logger.info(f"Connection established with {client_address}")
            client_socket.settimeout(2.0)

            try:
                # 5a. Receive data
                data = client_socket.recv(1024)
                if not data:
                    continue # If browser sent nothing, skip to the next loop

                # Parse the raw bytes into our HTTPRequest object
                request = HTTPRequest(data)

                response_bytes = router.handle_request(request)

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