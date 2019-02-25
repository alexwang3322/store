import argparse
from cvs_write import write_to_item_list_dataframe 



def calu_item_list(item_name, item_price, item_type="skis", express=70, binding_price=0, tariff=0.25):
    without_binding_package_price = item_price + express 
    with_binding_price = item_price + binding_price 
    package_all_price = item_price + binding_price + express
    import_with_tariff_prices = with_binding_price + with_binding_price * tariff
    
    write_to_item_list_dataframe(item_name, item_price, item_type, express, binding_price, 
                                with_binding_price, without_binding_package_price, package_all_price, import_with_tariff_prices)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--item_name", help="item name")
    parser.add_argument("-i", "--item_price", help="item price")
    parser.add_argument("-e", "--binding_price", help="binding price")

    args = parser.parse_args()

    ## settle or constants values-
    exchange_rate = 7.814
    item_name = args.item_name
    item_price = float(args.item_price)
    item_type = "skis"
    express = 70.0
    binding_price = float(args.binding_price)

    calu_item_list(item_name, item_price, binding_price=binding_price)
    
