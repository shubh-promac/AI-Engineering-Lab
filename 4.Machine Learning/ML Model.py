import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_data = pd.read_csv('4.Machine Learning/melb_data.csv') 
print(melbourne_data.columns)
# print(melbourne_data[melbourne_data.isna().any(axis=1)].to_string()) # checking how many nan values there are
melbourne_data = melbourne_data.dropna(axis=0) # we are dropping some values 

y = melbourne_data.Price
X = melbourne_data[['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']]
print(X.describe())
print(X.head())

'''
The 4 Steps of Modeling
The steps to building and using a model are:
~Define: Select the model type and configuration parameters.
~Fit: Train the model by capturing patterns from your data.
~Predict: Use the trained model to guess outcomes on data.
~Evaluate: Test the model to see how accurate it is.
'''

# DEFINE MODEL
melbourne_model = DecisionTreeRegressor(random_state=1) # Machine learning models use random numbers during training
# random_state is like a seed, getting you the same results every time you run the code
# A DecisionTreeRegressor is a model that predicts numerical values like house prices by splitting data into branches

# FIT MODEL
melbourne_model.fit(X, y)

# PREDICT MODEL
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head())) # predicting for only the first five
#print(f'My accuracy is {melbourne_model.evaluate()}')