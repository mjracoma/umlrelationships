import abc

class NotificationChannel(abc.ABC):
    @abc.abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationChannel):
    def send(self, message):
        print(f"Sending email notification: {message}")
        return True
    