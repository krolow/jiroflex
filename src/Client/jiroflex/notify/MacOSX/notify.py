import gntp.notifier

class Growl:
    
    def __init__(self, message = None):
        self.growl = gntp.notifier.GrowlNotifier(
            applicationName = "JiroFlex",
            notifications = ["New Messages"],
            defaultNotifications = ["New Messages"]
        )
        self.growl.register()
        self.message = message
        
    def send(self, message = None):
        if (message == None):
            message = self.message
            
        self.growl.notify(
            noteType = "New Messages",
            title = "JiroFlex",
            description = self.message,
            sticky = False,
            priority = 1
        )

        
        
        
