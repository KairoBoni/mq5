# -*- coding: utf-8 -*-
import MetaTrader5 as mt5


class MQ5Inicitalize:
    def apply():
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)
