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


del service

logger.log("Logger still works independently")
