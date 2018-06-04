import random
import pandas as pd
import numpy as np 

data_file = "final-result.csv"

train = pd.read_csv(data_file, header=0, delimiter=",")
ts =  train.shape 

df = pd.DataFrame(train)
new_train = df.reindex(np.random.permutation(df.index))

indice_70_percent = int((ts[0]/100.0)* 70)

new_train[indice_70_percent:].to_csv('train_data.csv', index=False, sep = ",")
new_train[:indice_70_percent].to_csv('test_data.csv', index=False, sep = ",")
