from Pickup_Items import *
from Item_store import *
def main():
    pickup_items = Pickup_items()
    aux_item_buy_list = []
    print("Balance Items")
    pickup_items.print_balance()

    #id_item, name_item, unit_price, quantity



    input_item_id = int(input("Enter Item Id that you want to buy: "))
    value_item_selected = pickup_items.get_item(input_item_id)
    value_item_selected
    input_item_quantity = int(input("Enter quantity that you want to buy: "))

    if(value_item_selected!=None):
        if(input_item_quantity <= value_item_selected.get_quantity()):
            aux_item_buy_list.append(Item_store(value_item_selected.get_id_item(), value_item_selected.get_name_item(),value_item_selected.get_unit_price(),input_item_quantity))


main()