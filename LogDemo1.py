import logging

logging.basicConfig(filename="C://df/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG
                    )

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is critical message")
