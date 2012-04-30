from config import CONFIG
from notify import notification
from rest import rest
import time
import datetime

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
                notification.Notify("Don't forget to start one task at Jira!")
                self.lastNotify = time.time()
    
    def __can_notify(self):
        return self.__check_interval() and self.__check_date() and self.__check_hour()
        
    def __check_interval(self):
        return time.time() > self.lastNotify + CONFIG['intervalNotifyStatus']
        
    def __check_date(self):
        print datetime.date.isoweekday(datetime.datetime.now())
        return datetime.date.isoweekday(datetime.datetime.now()) in CONFIG['days']
    
    def __check_hour(self):
        now = datetime.datetime.now()
        for hour in CONFIG['hours']:
            check = now.hour >= hour[0] and now.hour <= hour[1]
            if (check):
                return True   
        return False
        
        
jiroflex = Jiroflex()

if __name__ == "__main__":
    jiroflex.run()
