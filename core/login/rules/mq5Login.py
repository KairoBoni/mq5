# -*- coding: utf-8 -*-
import MetaTrader5 as mt5


class MQ5Login:
    def apply(user):
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
