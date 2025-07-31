import logging

# Step 1: Create a logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set the logging level

# Step 2: Create a file handler or console handler
file_handler = logging.FileHandler("app.log")   # Log messages to a file
console_handler = logging.StreamHandler()       # Log messages to the console

# Step 3: Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Step 4: Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Step 5: Logging messages
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")
