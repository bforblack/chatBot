import logging
logging.basicConfig(level=logging.INFO)

class ChatBotLogger:
     def info(self,info):
         logging.info(info)

     def error(self,error,e):
         logging.error(error,e)
