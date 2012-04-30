import sys
import pynotify

class Pynotify:

    def __init__(self, message = None):
        self.message = message

    def send(self, message = None):
        if (message == None):
            message = self.message
        pynotify.init('jiroflex')
        n = pynotify.Notification(
            "JiroFlex",
            self.message,
            "dialog-warning"
        )
        n.show()
