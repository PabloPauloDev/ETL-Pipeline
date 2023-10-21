import pandas as pd
import json

df = pd.read_csv('insurance.csv')

#extraction

agef = df.loc[(df['age'] >= 30) & (df['age'] <= 45)]
for index, sex in enumerate(agef['sex']):
    agef['sex'][index] = sex.title()

#Transforming

agef.to_csv('InsuranceMiddle.csv', index=False)

#Loading


