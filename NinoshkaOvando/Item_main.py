from Pickup_Items import *
from Item_store import *
def main():
    pickup_items = Pickup_items()
    aux_item_buy_list = []


    #id_item, name_item, unit_price, quantity

    continue_order=True
    while (continue_order):
        print("Balance Items")
        pickup_items.print_balance()
        input_item_id = int(input("Enter Item Id that you want to buy: "))
        value_item_selected = pickup_items.get_item(input_item_id)


        if(value_item_selected!=None):
            input_item_quantity = int(input("Enter quantity that you want to buy: "))
            if(input_item_quantity <= value_item_selected.get_quantity()):
                input_confirmation_order = int(input("Enter 1 if you want buy or enter 0 if you want to continue buy: "))
                if(input_confirmation_order == 1):
                    aux_item_buy_list.append(Item_store(value_item_selected.get_id_item(), value_item_selected.get_name_item(),value_item_selected.get_unit_price(),input_item_quantity))
                    print("Place order was completed!!")
                    total_amount= value_item_selected.get_unit_price()*input_item_quantity
                    print("Item ID: {},Item Name: {}, Unit Price: {}, Quantity: {}, total Amount: {}".format(value_item_selected.get_id_item(), value_item_selected.get_name_item(),value_item_selected.get_unit_price(),input_item_quantity, total_amount))
                    quatity_auxiliar1=value_item_selected.get_quantity()-input_item_quantity
                    print(pickup_items.set_quantity_item(value_item_selected.get_id_item(), quatity_auxiliar1))
                    confirmation_continue_order = int(input("Enter 1 if you want to continue buy or enter 0 if you want to exit "))
                    if (confirmation_continue_order == 1):
                        continue_order = True
                    elif(confirmation_continue_order == 0):
                        total_amount_buy= 0
                        for val in aux_item_buy_list:
                            total_a=val.get_unit_price()*val.get_quantity()
                            print("Item ID: {},Item Name: {}, Unit Price: {}, Quantity: {}, total Amount: {}".format(val.get_id_item(), val.get_name_item(),val.get_unit_price(),val.get_quantity(), total_a))
                            total_amount_buy = total_amount_buy + total_a
                        print("Your total amount is:", total_amount_buy)
                        continue_order = False
                    else:
                        confirmation_continue_order = int(
                            input("Enter 1 if you want to continue buy or enter 0 if you want to exit "))

                elif(input_confirmation_order == 0):
                    continue_order = True
                else:
                    confirmation_continue_order = int(
                        input("Enter 1 if you want to continue buy or enter 0 if you want to exit "))
            else:
                print("Please, your item number should be less than stock.")
        else:
            print("Please, select a Item Id existent")

main()