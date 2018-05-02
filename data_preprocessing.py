import numpy as np 
import matplotlib as plot
import pandas as pd 


dataset  = pd.read_csv('Data.csv')



x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1:].values


print(x)


from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

imputer = imputer.fit(x[:, 1:])

x[:, 1:] = imputer.transform(x[:, 1:])

print(x)