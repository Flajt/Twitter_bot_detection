from helper import preprocess
from helper import word_encoder
import model
import pandas as pd
import numpy as np


p=preprocess.preprocess()
c=word_encoder.encoder()

human_source="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.1k.csv"
bot_source="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.1k.csv"

human=p.read(human_source)
human=p.remove(human,"screen_name")
human=p.remove(human,"source_identity")
bot=p.read(bot_source)
bot=p.remove(bot,"screen_name")
bot=p.remove(bot,"source_identity")
x=pd.concat([bot,human])
bot_y=pd.DataFrame(c.create_new_array(shape=(1,len(bot)),replace=True,replace_with=1))
human_y=pd.DataFrame(c.create_new_array(shape=(1,len(bot)),replace=True,replace_with=0))
y=pd.concat([bot_y,human_y])
m=model.DFFP(checkpoint_path="./Models/checkpoint.ckpt",model_path="./Models/model1.tfl")
print(x)

#m.train(x,y)
