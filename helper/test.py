import preprocess


file="A://Github//Twitter_bot_detection//Datasets//classification_processed//humans//humans.1k.csv"
file2="A://Github//Twitter_bot_detection//Datasets//classification_processed//bots//bots.1k.csv"
p=preprocess.preprocess()
h=p.setup(file,"screen_name","source_identity")
b=p.setup(file2,"screen_name","source_identity")
print(p.combine_arrays(h,b).shape)
