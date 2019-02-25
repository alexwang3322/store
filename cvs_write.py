import pandas as pd
pd.set_option('display.width',1000)


#df_item_list = pd.read_csv('alpha-item_list.csv')


def write_to_item_list_dataframe(item_name, item_price, item_type, express, binding_price, 
                                with_binding_price, without_binding_package_price, package_all_price, import_with_tariff_prices, exchange_rate=7.814):
    #print item_name, item_price, item_type, express, binding_price, with_binding_price, without_binding_package_price, package_all_price, import_with_tariff_prices
    
    item = pd.Series({"item_name": item_name, 
                        "item_price": (item_price * exchange_rate, item_price), 
                        "item_type": item_type, 
                        "express": express, 
                        "binding_price": binding_price, 
                        "with_binding_price": (exchange_rate * with_binding_price, with_binding_price), 
                        "without_binding_package_price": (exchange_rate * without_binding_package_price, without_binding_package_price), 
                        "package_all_price": (exchange_rate * package_all_price, package_all_price),
                        "import_with_tariff_prices": (exchange_rate * import_with_tariff_prices, import_with_tariff_prices)}) 
    df_store = pd.read_csv("alpha-item_list.csv")
    new_df = df_store.append(item, ignore_index=True)
    write_item_list(new_df, 'alpha-item_list.csv')


def write_item_list(df, cvs_name):
    df.to_csv(cvs_name, header=False)


    