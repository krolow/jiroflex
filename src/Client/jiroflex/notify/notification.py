import sys

class Notify:
    
    def __init__(self, message = None):
        self.message = message
        getattr(self, sys.platform)()
        self.send()
        
    def darwin(self):
        from MacOSX import notify
        self.notify = notify.Growl(self.message)
         
    def linux32(self):
        from Linux import notify
        
    def win32(self):
        from Windows import notify
        
    def send(self):
        self.notify.send(self.message)

        
        
