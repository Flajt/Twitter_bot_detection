import pandas as pd
import os
import numpy
numpy.set_printoptions(threshold=numpy.nan)
os.chdir("A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//")
f=pd.read_csv("A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.1k.csv")
print(len(f.values[0]))
del f["screen_name"]
del f["source_identity"]
print(len(numpy.round(f.values[0])))
