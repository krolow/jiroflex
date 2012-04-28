CONFIG = {    
    #what days should we check? 1 = Sunday...
    'days' : [
        2,
        3,
        4,
        5,
        6
    ],
   
    #between each time should we check? 8 = 8am 13 = 1pm
    'hours' : [
        [8, 12],
        [13, 18]
    ],

    #interval in seconds to check the status of one task
    'intervalCheckStatus' : 5,
    
    #interval in seconds to notify that one task is stopped
    'intervalNotifyStatus' : 60,
    
    #jira REST URL
    'url' : 'http://127.0.0.1:5000',
    
    #your jira username
    'username' : 'vkrolow'
};