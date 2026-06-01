import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

"""
The Concept: max_leaf_nodes
We can optimize the model by setting a limit on the number of "leaves" (final prediction points) the tree is allowed to make.
Too few leaves (e.g., 5): The model is too simple. It treats vastly different houses the same way (Underfitting).
Too many leaves (e.g., 5,000): The model gets distracted by random patterns and noise (Overfitting).
The Sweet Spot (e.g., 500): The model captures the real patterns without memorizing the noise.

Why Use It
Prevents Overfitting: Without a limit, a decision tree will keep splitting until every training point is perfectly isolated, leading to high variance.
Improves Generalization: Restricting the leaves forces the model to capture only the most important patterns, which usually helps it perform better on unseen validation data.
Balances Complexity: It offers a finer, more stable way to control tree depth compared to max_depth.
"""

melbourne_data = pd.read_csv('4.Machine Learning/Datasets/melb_data.csv') 
filtered_melbourne_data = melbourne_data.dropna(axis=0)
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {max_leaf_nodes:4}  ->  Mean Absolute Error: ${my_mae:,.2f}") #commas(,) for thousands and rounds it to 2 decimal places(.2f).
# .2 means exactly 2 decimal places, the f stands for Fixed-point, which treats the number like a float (not standard form).


'''
Here's the takeaway: Models can suffer from either:
~Overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions, or
~Underfitting: failing to capture relevant patterns, again leading to less accurate predictions.
We use validation data, which isn't used in model training, to measure a candidate model's accuracy.
This lets us try many candidate models and keep the best one.
'''