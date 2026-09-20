from src.config import HOST, PORT
from src.utils.logger import logger

def main():
    logger.info("Initializing Secure File Sharing Server...")
    logger.info(f"COnfiguration loaded: Binding to {HOST}:{PORT}")

    try:
        logger.debug("Server loop would start here.")
    except Exception as e:
        logger.error(f"A fatal error occurred: {e}, exc_info=True")
    finally:
        logger.info("Server shutting down.")

if __name__== "__main__":
    main()