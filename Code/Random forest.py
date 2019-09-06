#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

# Import the libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df  = pd.read_excel('book1.xlsx',sep=",",header=None)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header

data = df.iloc[:,:5]
label = df.iloc[:,5:]
number = LabelEncoder()
data['prior sign'] = number.fit_transform(data['prior sign'].astype('str'))
data['mental illness'] = number.fit_transform(data['mental illness'].astype('str'))
data['Race'] = number.fit_transform(data['Race'].astype('str'))
data['weapon possessed'] = number.fit_transform(data['weapon possessed'].astype('str'))

train_features, test_features, train_labels, test_labels = train_test_split(data, label, 
                                                                            test_size = 0.3, 
                                                                            random_state = 42)
train_labels=train_labels.astype('int')
test_labels=test_labels.astype('int')

#applying Random forest regressor
model = RandomForestRegressor(n_jobs=-1)
estimators = np.arange(10, 200, 10)
scores = []
for n in estimators:
    model.set_params(n_estimators=n)
    model.fit(train_features, np.ravel(train_labels))
    scores.append(model.score(test_features, test_labels))

print(model.score(train_features, train_labels))

