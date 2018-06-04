import pandas as pd
 
data_file = "final-result.csv"

data = pd.read_csv(data_file, sep=',')

odd_sample = data.loc[1::2]
even_sample = data.loc[::2]

odd_sample.to_csv('sample-odd.csv', index=False, sep=',')
even_sample.to_csv('sample-even.csv', index=False, sep=',')

