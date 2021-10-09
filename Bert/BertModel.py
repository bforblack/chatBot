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


    def getTokenizedData(self,data,max_length=128):
        input_dic=tokenizer._encode_plus(data,add_special_tokens=True,max_length=max_length,return_token_type_ids=True,
                                         return_attention_mask=True,truncation_strategy=True,padding_strategy=True)

        input_ids,attention_mask,token_type_ids=(input_dic['input_ids'],input_dic['attention_mask'],input_dic['token_type_ids'])

        return InputFeatures(input_ids=input_ids,attention_mask=attention_mask,token_type_ids=token_type_ids)




    def generateTensorData(self,features):
        def gen():
            for f in features:
                yield (
                    {
                        "input_ids": f.input_ids,
                        "attention_mask": f.attention_mask,
                        "token_type_ids": f.token_type_ids,
                    },
                    f.label,
                )

        return  tf.data.Dataset.from_generator(
        gen,
        ({"input_ids": tf.int32, "attention_mask": tf.int32, "token_type_ids": tf.int32}, tf.int64),
        (
            {
                "input_ids": tf.TensorShape([None]),
                "attention_mask": tf.TensorShape([None]),
                "token_type_ids": tf.TensorShape([None]),
            },
            tf.TensorShape([]),
        ),
    )










