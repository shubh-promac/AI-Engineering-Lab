import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_data = pd.read_csv('4.Machine Learning/Datasets/melb_data.csv') 
melbourne_data = melbourne_data.dropna(axis=0) 

y = melbourne_data.Price
X = melbourne_data[['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

'''
The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree.
It generally has much better predictive accuracy than a single decision tree and it works well with default parameters.

~A Decision Tree is like asking one expert for advice. If that expert has a specific bias or had bad data, their advice might be wrong.
~A Random Forest is like asking a committee of 100 experts (trees) to vote.
 Each expert looks at the problem from a slightly different angle, and the final decision is based on the average of all their answers.

How the "Forest" is Built (The "Random" Part)
If you train 100 identical trees on the same data, they will all make the exact same mistakes.
To make the trees different and unique, Random Forest introduces randomness in two ways:
~Random Rows (Bootstrapping / Bagging): Each tree is trained on a random sample of the dataset.
 Some rows of data are repeated, and some are left out completely. No two trees see the exact same dataset.
~Random Columns (Feature Subsampling): When a tree is deciding how to split data (e.g., splitting by number of rooms vs. land size),
 it is only allowed to choose from a random handful of features, not all of them.
'''

# MODEL A: YOUR BEST DECISION TREE
tree_model = DecisionTreeRegressor(max_leaf_nodes=500, random_state=1)
tree_model.fit(train_X, train_y)
tree_preds = tree_model.predict(val_X)
tree_mae = mean_absolute_error(val_y, tree_preds)

# MODEL B: NEW RANDOM FOREST MODEL
# n_estimators=100 means it creates 100 individual trees behind the scenes
rf_model = RandomForestRegressor(n_estimators=100, random_state=1)
rf_model.fit(train_X, train_y)
rf_preds = rf_model.predict(val_X)
rf_mae = mean_absolute_error(val_y, rf_preds)

print("--- Performance Head-to-Head ---")
print(f"Optimal Decision Tree MAE: ${tree_mae:,.2f}")
print(f"Random Forest Regressor MAE: ${rf_mae:,.2f}")

'''
~n_estimators
The total number of individual decision trees you build in your forest. This is the number of experts sitting in your committee room.

~max_depth
The maximum depth of each tree. Limiting depth (e.g., max_depth=10) stops trees from splitting indefinitely, which reduces file size and prevents overfitting.
The maximum number of consecutive questions any single tree is allowed to ask. This is how deep an expert is allowed to interrogate a single house profile.

~min_samples_split
The minimum number of data points required to split a node.
Setting this higher (e.g., 5 or 10) stops trees from creating highly specific rules for just 1 or 2 houses.
The minimum number of houses required in a group before a tree is allowed to split them further.
This is the rule that says, "You cannot make up a specific pricing rule unless it applies to a decent-sized group of houses."

~max_features
The number of columns each tree looks at. Setting this to 'sqrt' means each tree only checks the square root of the total features at each split,
forcing maximum variety.
The maximum number of columns (features) a single tree is allowed to choose from when making a decision.
This is like restricting the information given to each expert so they don't all look at the exact same details.
'''

# A finely-tuned, robust forest configuration
rf_model = RandomForestRegressor(
    n_estimators=200,      # Use 200 trees instead of 100
    max_depth=15,          # Cap tree depth to prevent massive file sizes
    min_samples_split=5,   # Require 5 houses to create a new rule branch
    random_state=1,
    n_jobs=-1              # Use ALL CPU cores on your computer to train in parallel
)
# n_jobs=-1 tells the model to use all available CPU cores, which can significantly speed up training time, especially with a large number of trees (n_estimators).
# but only use this on large datasets and if you have a multi-core processor, otherwise it may not provide a speed boost and could even slow down training on small datasets.

rf_model.fit(train_X, train_y)
# Importance Scores: A hypothetical output list showing percentage breakdowns to visually demonstrate how the model ranks variables.

# Extract the importance scores
importances = rf_model.feature_importances_

# Pair the scores with the column names
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.2%}") # % tell it to treat the number like a percentage