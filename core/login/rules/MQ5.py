# -*- coding: utf-8 -*-
import MetaTrader5 as mt5
import pandas as pd
from entity.User import User


def MQ5Inicitalize():
    print("MetaTrader5 package author: ", mt5.__author__)
    print("MetaTrader5 package version: ", mt5.__version__)


def MQ5Login(user: User):
    if not mt5.initialize(
            login=user.id,
            server=user.server,
            password=user.password
    ):
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    # conectamo-nos à conta de negociação sem especificar senha e servidor
    authorized = mt5.login(
        user.id,
        password=user.password,
        server=user.server
    )

    return authorized


def AccountStatus():
    account_info = mt5.account_info()
    if account_info is not None:
        print(account_info)
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))

        df = pd.DataFrame(
            list(account_info_dict.items()), columns=['property', 'value']
        )

        print("account_info() as dataframe:")
        print(df)
    else:
        print("failed to get account info")


def GetSell(fromDate, quantity, symbol):
    ticks = mt5.copy_ticks_from(symbol, fromDate, quantity, 2)
    
    # exibimos cada tick numa nova linha
    print("Exibimos os ticks recebidos como são")
    count = 0
    for tick in ticks:
        count+=1
        print(tick)
        if count >= 10:
            break

    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1500)

    ticks_frame = pd.DataFrame(ticks)

    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    print("\nExibimos o dataframe com ticks")
    print(ticks_frame.head(10))
