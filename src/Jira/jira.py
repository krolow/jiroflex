import SOAPpy, getpass, datetime

class Jira:

    def __init__(self, url, login, password):
        self.soap = SOAPpy.WSDL.Proxy(url)
        self.auth = self.soap.login(login, password);
        
    def listSOAPmethods(self):
        for key in self.soap.methods.keys():
            print key, ': '
            for param in self.soap.methods[key].inparams:
                print '\t', param.name.ljust(10), param.type
            for param in self.soap.methods[key].outparams:
                print '\tOut: ', param.name.ljust(10), param.type
                
    def hasTaskInProgress(self, username):
        query = 'assignee = "%s" AND status = "In Progress"' % (username)
        results = SOAPpy.Types.intType(int(1))
        tasks = self.soap.getIssuesFromJqlSearch(self.auth, query, results)
        
        if len(tasks)  == 1:
            return True
            
        return False