import SOAPpy, getpass, datetime

class Jira:

    def __init__(self, url, username, password):
        self.soap = SOAPpy.WSDL.Proxy(url)
        self.url = url;
        self.username = username
        self.password = password
        self.login();
    
    def login(self):
        self.auth = self.soap.login(self.username, self.password);
        
    def list_soap_methods(self):
        for key in self.soap.methods.keys():
            print key, ': '
            for param in self.soap.methods[key].inparams:
                print '\t', param.name.ljust(10), param.type
            for param in self.soap.methods[key].outparams:
                print '\tOut: ', param.name.ljust(10), param.type
                
    def has_task_in_progress(self, username):
        query = 'assignee = "%s" AND status = "In Progress"' % (username)
        results = SOAPpy.Types.intType(int(1))
        try:
            tasks = self.soap.getIssuesFromJqlSearch(self.auth, query, results)
        except:
            self.login()
            self.has_task_in_progress(self, username)
            
        if len(tasks)  == 1:
            return True
            
        return False
    
    def logout(self):
        self.soap.logout(self.auth)

        
        