class Logger:
    def log(self, message):
        print(f"[LOG] {message}")


class Service:
    def __init__(self, payload):
        self.payload = payload

    def process(self, logger):
        logger.log(f"Processing {self.payload}")

logger = Logger()
service = Service("order_101")
service.process(logger)

# Notice: The Service does not own the Logger.
# Even if the Service object is deleted, the Logger still exists.

del service

logger.log("Logger still works independently")