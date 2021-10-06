import pandas as pd
import config
from Storage.DatabaseConnector import Storage
from transformers import TFAutoModelForSequenceClassification,BertTokenizer,InputExample,InputFeatures
import pandas as pd
import  tensorflow as tf


model=TFAutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
tokenizer=BertTokenizer.from_pretrained('bert-base-uncased')



class Sentiment:
    def __init__(self,model):
        model=model



    def trainModle(self,train_data,validation_data):
      model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5),
        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics = tf.metrics.SparseCategoricalAccuracy(),)

      model.fit(train_data,validation_data=validation_data,epochs=3)
      self.model=model
      Storage.insertModel(model)


    def predictSetiment(self,data_to_bePredicted):
        model_outPut=model(data_to_bePredicted)
        tf_output=tf.nn.softmax(model_outPut[0],axis=-1)
        return tf_output


    def createInputData(self,data):
        return InputExample(guid=None,text_a=data['Reviews'],text_b=None,label=data['Sentiments'])


    def createFeature(self,data):
        return None

















