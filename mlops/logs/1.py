import logging

# Configure logging to store logs in a file
logging.basicConfig(
    filename='/Users/ramrekhayadav/mlops/python/mlops/logs/app.log',  # Log file name
    level=logging.DEBUG,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

def log_messages():
    """Logs messages of different severity levels."""
    try:
        logging.debug("This is a debug message")
        logging.info("This is an info message")
        logging.warning("This is a warning message")
        # Simulate an error
        x = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.error("An error occurred: %s", e)
        logging.critical("Critical issue encountered!")


log_messages()