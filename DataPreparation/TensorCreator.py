import pandas as pd
from logger import logging


class TensorData:
    def __init__(self,testData,trainData):
        if testData!=None:
            self.test_data=testData
            count=len(pd.DataFrame(trainData).index)
            count_validation=count*20/100
            self.validation_data=trainData[:count_validation]
            self.train_data=trainData[count_validation:]

        else:
            count =len(pd.DataFrame(trainData).index)
            test_count=count*30/100
            train_count=count-testData
            validation_count=train_count*20/100
            self.test_data=trainData[:test_count]
            train=trainData[test_count:]
            self.validation_data=train[:validation_count]
            self.train_data=train[validation_count:]

        logging.info("-------Test Data Shape-------",self.test_data.shape)
        logging.info("-------Train Data Shape-------", self.train_data_data.shape)
        logging.info("-------Validation Data Shape-------", self.validation_data.shape)



    def processedData(self,data):
        return self.train_data,self.validation_data,self.test_data

