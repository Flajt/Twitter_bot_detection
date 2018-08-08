import model
from helper import preprocess, word_encoder
import numpy as np
import pandas as pd

file=input("Enter the file path:")
p=preprocess.preprocess()
c=word_encoder.encoder()
m=model.DFFP(checkpoint_path="./Models/checkpoint.ckpt",model_path="./Models/model5_withdropout.tfl")
try:
    x=p.setup(file,"screen_name","source_identity")
except Exception as e:
    print("[!]: Warning: {}".format(e))
try:
    print(m._predict(x))
except Exception as e:
    print("[!]: Warning: {}".format(e))
    print("Try to run 1 possible salution...(reshape them)")
    try:
        print(m._predict(x.reshape((1,14))))
    except Exception as e:
        print("[!]: Warning: {}".format(e))
        print("If haven`t used a valid file, please try againe.\n If that doesn`t work please contact me at Github via an issue! ")
