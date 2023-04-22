import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split


def split_data(X, y, test_size=0.2, random_state=0):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
