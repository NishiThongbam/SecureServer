from src.config import HOST, PORT, MAX_CONNECTIONS
from src.utils.logger import logger

from src.server import start_server

def main():
    logger.info("Initializing Secure File Sharing Server...")
    
    logger.debug(f"MAx COnnections Possible: {MAX_CONNECTIONS}")

    try:
        start_server()
    except KeyboardInterrupt:
        logger.info("Server interrupted by user. ")
    except Exception as e:
        logger.error(f"A fatal error occurred: {e}", exc_info=True)
    finally:
        logger.info("Server shutting down. ")

    

if __name__== "__main__":
    main()