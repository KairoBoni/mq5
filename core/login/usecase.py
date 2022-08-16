# -*- coding: utf-8 -*-

import rules.MQ5 as mq5
from entity.User import User


class UseCase:
    def execute(self, user: User):
        mq5.MQ5Inicitalize()

        isAuth = mq5.MQ5Login(user)

        if isAuth:
            mq5.AccountStatus()
        else:
            print("failed to connect")
