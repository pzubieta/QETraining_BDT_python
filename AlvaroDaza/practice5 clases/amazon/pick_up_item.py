import log
import store.store

logger = log.setup_custom_logger(__name__)

sales = 0

best_buy = store.store.Store("best buy")
print(best_buy.get_store_name())
logger.info('Creating Items')
best_buy.add_item('Accione', 150.0, 50)
best_buy.add_item('Bass one', 50.0, 100)
best_buy.add_item('Accione P', 300.0, 10)
logger.info('Show Items')
best_buy.show_total_products()

item_name = raw_input("which product do you want purchase?")
item_amount = int(raw_input('how many do you want purchase'))
sales = best_buy.sell_item(item_name, item_amount)
print('====Was sold:' + str(sales) + '$ ====')
best_buy.show_total_products()
