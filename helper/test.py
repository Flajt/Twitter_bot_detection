import preprocess
import pandas as pd

f=pd.read_csv("A:\\Github\\Twitter_bot_detection\\Datasets\\classification_processed\\humans\\humans.1k.csv")
p=preprocess.preprocess()
f=p.remove(f,"screen_name")
f=p.remove(f,"source_identity")

#f=p.remove(f,"")
