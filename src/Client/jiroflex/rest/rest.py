import urllib2
import json

class Rest:
    
    def __init__(self, url, username):
        self.url = url
        self.username = username
        
    def get_current_status(self):
        data = json.load(urllib2.urlopen(self.url + '/progress/' + self.username));
        
        return data['progress']