from pymongo import MongoClient
import config
from logger import logging



#client=MongoClinet(config.data_base_ip,config.data_base_port)

class Storage:
    def __init__(self):
        try:
            self.client=MongoClient(config.data_base_ip,config.data_base_port)
            logging.info("----Data  Base connected Sucessfully-------")
        except Exception as e:
            logging.error('---Exception Was Caught while Generating Connection With Db With Cause',e.__cause__,e)

    def insertData(self,data):
       try:
        self.client.isert_many(data)
        logging.info('---Data Was Inserted Sucessfully----')
       except Exception as e:
           logging.error('---Exception Was Caught While Inserting data into Data with cause',e.__cause__,e)

    def insertModel(self,model):
        try:
            self.client.insert(model)
            logging.info('---Model Was Inserted Sucessfully----')
        except Exception as e:
            logging.error('---Exception Was Caught While Inserting data into Data with cause', e.__cause__, e)




