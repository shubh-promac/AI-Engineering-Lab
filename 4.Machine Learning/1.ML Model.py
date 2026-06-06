import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_data = pd.read_csv('4.Machine Learning/Datasets/melb_data.csv') 
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
melbourne_model.fit(X, y) # look at X and try to predict y, think of it like y = f(X) you have X but now you have to work out y

# PREDICT MODEL
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head())) # predicting for only the first five

# EVALUATE MODEL
# What is Model Validation

# error=actual−predicted
prediction = melbourne_model.predict(X)
mean_absolute_error(y, prediction)

# The Problem with "In-Sample" Scores
# mean_absolute_error computes this using the same data on which the model was trained on
# Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used to build the model.
# The most straightforward way to do this is to exclude some data from the model-building process,
# and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.
# The scikit-learn library has a function train_test_split to break up the data into two pieces.
# We'll use some of that data as training data to fit the model, and we'll use the other data as validation data to calculate mean_absolute_error


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
# The Split: 75% becomes the "Study Guide" (train_X and train_y).
# The other 25% becomes the "Final Exam" (val_X and val_y).
# You lock the exam in a drawer so the AI can't cheat.
# train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1, test_size=0.20) setting 80% as the study guide and 20% as the final exam
# train_X : The questions on the study guide.
# train_y : The answers on the study guide.
# val_X : The questions on the final exam.
# val_y : The answer key to the final exam.
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions)) # this is how much it gets the prices wrong by the range
# You pull the Final Exam answer key (val_y) out of the drawer.
# You compare the AI's guesses to the actual prices to see how many dollars off it was on average.
# This gives you its true, honest score.