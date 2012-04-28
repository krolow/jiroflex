from config import CONFIG
from notify import notification
from rest import rest
import time

class Jiroflex:
    
    lastNotify = 0
    
    def __init__(self):
        self.rest = rest.Rest(CONFIG['url'], CONFIG['username'])
        
    def run(self):
        while True:
            self.notify()
            time.sleep(CONFIG['intervalCheckStatus'])
    
    def notify(self):
        if (self.__can_notify()):
            status = self.rest.get_current_status()
            if (status == False):
                notification.Notify("Don't forget to start one task at Jira:")
                self.lastNotify = time.time()
    
    def __can_notify(self):
        return time.time() > self.lastNotify + CONFIG['intervalNotifyStatus']
        

jiroflex = Jiroflex()

if __name__ == "__main__":
    jiroflex.run()
