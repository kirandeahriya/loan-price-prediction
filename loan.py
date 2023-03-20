import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

train=pd.read_csv("train_u6lujuX_CVtuZ9i.csv")
test=pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")

train_original=train.copy()
test_original=test.copy()


print("Data Types  of Train Data Set")
print(train.dtypes)

print("Attributes of Test Data Set")
print(test.columns)

print("Data Types  of Test Data Set")
print(test.dtypes)

print("Row n Col of train")
print(train.shape)

print("Row n Col of test")
print(test.shape)

print("Univariate Analysis train")
print(train['Loan_Status'].value_counts())

print("Univariate Analysis test")
print(test['Gender'].value_counts())

print(train['Loan_Status'].value_counts().plot.bar())
plt.show()

plt.figure(1)
plt.subplot(221)
train['Gender'].value_counts(normalize=True).plot.bar(figsize=(20,10), title= 'Gender')
plt.subplot(222)
train['Married'].value_counts(normalize=True).plot.bar(title= 'Married')
plt.subplot(223)
train['Self_Employed'].value_counts(normalize=True).plot.bar(title= 'Self_Employed')
plt.subplot(224)
train['Credit_History'].value_counts(normalize=True).plot.bar(title= 'Credit_History')
plt.show()