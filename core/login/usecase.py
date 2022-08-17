# -*- coding: utf-8 -*-
from datetime import datetime
import rules.MQ5 as mq5
from entity.User import User
import pytz


class UseCase:
    def execute(self, user: User):
        mq5.MQ5Inicitalize()

        isAuth = mq5.MQ5Login(user)

        if isAuth:
            mq5.AccountStatus()
            timezone = pytz.timezone("Etc/UTC")
            utc_from = datetime(2022, 8, 16, tzinfo=timezone)
            mq5.GetSell(utc_from, 100000, "USDJPY")

        else:
            print("failed to connect")


user = User(60146982, "urdaxv0f", "MetaQuotes-Demo")
useCase = UseCase()
useCase.execute(user)
