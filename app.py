import logging
import logging.config
import yaml
import os
from business.business import ShopingCart

if not os.path.exists('logs'):
    os.mkdir('logs')

with open('logging.yaml','r',encoding='utf-8') as f:
    config = yaml.load(f)
    logging.config.dictConfig(config)

logging.debug('Program start')
try:
    logging.info('Build ShoppingCart')
    shoping_cart = ShopingCart()
    shoping_cart.put('apple')
    shoping_cart_count = shoping_cart.get_count()
except Exception as e:
    logging.error('Error',exc_info=True)