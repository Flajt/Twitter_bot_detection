from helper import preprocess
import model

p=preprocess.preprocess()

human_source="./classification_processed/humans.1k.csv"
bot_source="./classification_processed/bots.1k.csv"

human=p.read(human_source)
bot=p.read(bot_source)
m=model.DFFP(checkpoint_path="./Models/checkpoint.ckpt",model_path="./Models/model1.tfl")
#m.train()
