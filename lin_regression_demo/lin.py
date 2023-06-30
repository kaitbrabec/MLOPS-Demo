import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

raw_data = pd.read_csv('Housing-3.csv')


x = raw_data[["area","bedrooms", "bathrooms", "stories"]]

y = raw_data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

model = LinearRegression()

model.fit(x_train, y_train)

predictions = model.predict(x_test)

