from MauricioZelaya.online_shopping.loggin_module import *
from MauricioZelaya.online_shopping.shopping_cart import shopping_cart

login_msg("info", "Initializing Shopping cart.............")
my_cart = shopping_cart()
login_msg("info", "adding items to inventory list.............")
my_cart.set_list_of_items("cellphone", 750.5, 2)
my_cart.set_list_of_items("usb charger", 50.0, 3)
my_cart.set_list_of_items("cellphone", 750.5, 2)
login_msg("debug", "products added.............")
login_msg("debug", my_cart.get_items_list())
print("********************************************************************************")
print("*                      ITEM and PRICE LIST                                     *")
print("********************************************************************************")
login_msg("info", "list prices.............")
for item in my_cart.get_items_list():
    print(item)
print("********************************************************************************")
print("*                      Buy a cellphone and a charger                           *")
print("********************************************************************************")
login_msg("info", "buying products.............")
my_cart.add_item_to_cart("cellphone", 750.5, 1)
my_cart.add_item_to_cart("usb charger", 50.0, 1)
login_msg("debug", "products bought.............")
login_msg("debug", my_cart.get_items_into_cart_list())
for item in my_cart.get_items_into_cart_list():
    print(item)
print("total amount to pay: %s $" % my_cart.get_total_amount_to_pay())
print("********************************************************************************")
print("*                      ITEMS REMAINING IN LIST                                 *")
print("********************************************************************************")
for item in my_cart.get_items_list():
    print(item)

