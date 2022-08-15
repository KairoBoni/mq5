import MetaTrader5 as mt5
import pandas as pd

class AccountStatus:
    def apply():
        account_info = mt5.account_info()
        if account_info != None:
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
