import logging
import time

class ShopingCart(object):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger('main.business')
    
    def put(self,commodity:str):
        self.logger.info('Put a %s',commodity)
        while(True):
            try:
                self.logger.debug('%s build',commodity)
                commodity.build()
            except Exception as e:
                self.logger.error('Put apple failed',exc_info=True)
                self.logger.info('Put a apple failed')
            time.sleep(5)