from helper import preprocess,word_encoder
import model
import pandas as pd
import numpy as np


p=preprocess.preprocess()
c=word_encoder.encoder()
human_source="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.1k.csv"
human_s2="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.1M.csv"
human_s3="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.10M.csv"
human_s4="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.100k.csv"
bot_source="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.1k.csv"
bot_s2="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.1M.csv"
bot_s3="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.10M.csv"
bot_s4="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.100k.csv"
human=p.setup(human_source,"screen_name","source_identity")
bot=p.setup(bot_source,"screen_name","source_identity")
bot_2=p.setup(bot_s2,"screen_name","source_identity")
bot_3=p.setup(bot_s3,"screen_name","source_identity")
bot_4=p.setup(bot_s4,"screen_name","source_identity")
human_2=p.setup(human_s2,"screen_name","source_identity")
human_3=p.setup(human_s3,"screen_name","source_identity")
human_4=p.setup(human_s4,"screen_name","source_identity")
x=p.combine_arrays(human,bot)
x_2=p.combine_arrays(human_2,bot_2)
x_3=p.combine_arrays(human_3,bot_3)
x_4=p.combine_arrays(human_4,bot_4)
x=p.combine_arrays(x,x_2)
x=p.combine_arrays(x,x_3)
#x=p.combine_arrays(x,x_4)
bot_y=pd.DataFrame(c.create_new_array(shape=(1,len(bot)),replace=True,replace_with=1)).values
bot_y2=pd.DataFrame(c.create_new_array(shape=(1,len(bot_2)),replace=True,replace_with=1)).values
bot_y3=pd.DataFrame(c.create_new_array(shape=(1,len(bot_3)),replace=True,replace_with=1)).values
bot_y4=pd.DataFrame(c.create_new_array(shape=(1,len(bot_4)),replace=True,replace_with=1)).values
human_y=pd.DataFrame(c.create_new_array(shape=(1,len(human)),replace=True,replace_with=0)).values
human_y2=pd.DataFrame(c.create_new_array(shape=(1,len(human_2)),replace=True,replace_with=0)).values
human_y3=pd.DataFrame(c.create_new_array(shape=(1,len(human_3)),replace=True,replace_with=0)).values
human_y4=pd.DataFrame(c.create_new_array(shape=(1,len(human_4)),replace=True,replace_with=0)).values
y=np.column_stack((human_y,bot_y))
y2=np.column_stack((human_y2,bot_y2))
y3=np.column_stack((human_y3,bot_y3))
y4=np.column_stack((human_y4,bot_y4))
Y=np.column_stack((y,y2))
Y=np.column_stack((Y,y3))
#Y=np.column_stack((Y,y4))
evaluate=p.combine_arrays(human_4,bot_4)
m=model.DFFP(checkpoint_path="./Models/checkpoint.ckpt",model_path="./Models/model5_withdropout.tfl")
#m.train(x,Y.T,n_e=120)
path="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.100k.csv"
path_2="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.100k.csv"
x=p.setup(path,"screen_name","source_identity")
x2=p.setup(path_2,"screen_name","source_identity")
x=x2[1].reshape((1,14))
#print(m._predict(x))
print(m.evaluate(evaluate,y4.T))
