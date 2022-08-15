# -*- coding: utf-8 -*-

class UseCase:
    
    def __init__(self, mQ5Inicitalize, mQ5Login):
        self.mQ5Inicitalize = MQ5Inicitalize()
        self.mQ5Login = MQ5Login()
        self.accountStatus = AccountStatus()
    
    def execute(self, user):
        self.mQ5Inicitalize.apply()
        
        isAuth = self.mQ5Login.apply(user)
        
        if isAuth:
            self.accountStatus.apply()

        else:
            print("failed to connect")
