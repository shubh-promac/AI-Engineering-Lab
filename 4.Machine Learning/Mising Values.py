import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer 
from sklearn.impute import IterativeImputer
'''
There are three main approaches to handling missing values in machine learning:
1. Drop the columns with missing values
- Unless most values in the dropped columns are missing, the model loses access to a lot of (potentially useful!) information with this approach.
As an extreme example, consider a dataset with 10,000 rows, where one important column is missing a single entry. This approach would drop the column entirely!

2. Impute the missing values with a constant value (e.g., 0)
- Imputation fills in the missing values with some number. For instance, we can fill in the mean value along each column.
- The imputed value won't be exactly right in most cases, but it usually leads to more accurate models than you would get from dropping the column entirely.

3. An Extension To Imputation
- Imputed values may be systematically above or below their actual values (which weren't collected in the dataset).
- Or rows with missing values may be unique in some other way. In that case, your model would make better predictions by considering which values were originally missing.
- In this approach, we impute the missing values, as before. And, additionally, for each column with missing entries in the original dataset, we add a new column that shows the location of the imputed entries.
- there will be another column beside it containing values ranging from either true or false, true represents that this value has been imputated
'''

data = pd.read_csv('4.Machine Learning/Datasets/melb_data.csv')
y = data.Price # Select target

# To keep things simple, we'll use only numerical predictors
melb_predictors = data.drop(['Price'], axis=1)
X = melb_predictors.select_dtypes(exclude=['object']) # removes all the text columns from your data and keeps only the number columns.

# Divide data into training and validation subsets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

def get_mae(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Get names of columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

print("MAE from Approach 1 (Drop columns with missing values):")
print(get_mae(reduced_X_train, reduced_X_valid, y_train, y_valid))



# Approach 2: Imputation
# we can change strategy to 'median', 'most_frequent' or 'constant' then put fill_value= anything you would like to replcae it with
my_imputer = SimpleImputer(strategy='mean') # By default, it finds missing values (NaN) and replaces them witthe mean (average) value of that specific column.
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train), index=X_train.index) 
# The imputer calcutes the average values using the training data (X_train) and immediately fills its missing spots.
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid), index=X_valid.index) # pyright: ignore[reportArgumentType]
# The imputer uses those exact same calculated averages to fill the missing spots in the validation data (X_valid).

# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns # Copies the original column headers back onto the newly filled training data.
imputed_X_valid.columns = X_valid.columns # Copies the original column headers back onto the newly filled validation data.

print("MAE from Approach 2 (Imputation):")
print(get_mae(imputed_X_train, imputed_X_valid, y_train, y_valid)) # asses the cleaned data into a custom function to calculate the Mean Absolute Error (MAE).


# Approach 3: Imputation with Missing Indicator

# add_indicator=True is useful when data is missing for a specific reason, rather than just by random accident. In data science, this is called MNAR (Missing Not At Random).
# otherwise it will slow the model down even further. It will try to find a pattern linking missing values to house prices.

# where it is actually useful
# Imagine factory machines fitted with a Temperature Sensor.
# Suddenly, the sensor stops sending data, leaving blanks in the log.
# Why it's missing: The machine got so hot that the sensor melted and broke down.
# The Clue: The missing data is an immediate warning that the machine is overheating.
# How it helps: The model sees the missing indicator flag and can predict a machine failure before it happens.

# Create the imputer with the tracking flag turned on
indicator_imputer = SimpleImputer(strategy='mean', add_indicator=True)

# This returns a numpy array, which we turn back into a DataFrame
imputed_X_plus = pd.DataFrame(indicator_imputer.fit_transform(X_train), index=X_train.index)
imputed_X_valid_plus = pd.DataFrame(indicator_imputer.transform(X_valid), index=X_valid.index) # pyright: ignore[reportArgumentType]

print("MAE from Approach 3 (An Extension to Imputation):")
print(get_mae(imputed_X_plus, imputed_X_valid_plus, y_train, y_valid))


# Approach 4: Iterative Imputation (Smart ML Guessing)
'''
🎨 The Analogy: The Detective Group Project
Imagine three students work together on a project, but each accidentally drops one piece of their data:
-Student A loses their Salary data.
-Student B loses their House Size data.
-Student C loses their Zip Code data.

How a SimpleImputer solves it:
It looks at Student A, shrugs, and gives them the exact average salary of the entire country. It doesn't look at their big house or expensive zip code. It's a lazy guess.
How an IterativeImputer solves it:
It builds a mini AI model for each person using the remaining clues:
Round 1: It looks at Student A's House Size and Zip Code, realizes they live in a luxury neighborhood, and predicts a high Salary for them.
Round 2: Now that Salary is filled, it uses that new salary data to go back and make an even more accurate guess for Student B's missing House Size.
Round 3: It repeats this cycle (iterates) several times until the guesses stabilize and stop changing.
'''

# Create the smart imputer that models missing features based on others
# max_iter=10 means it will pass through the data 10 times to refine its guesses
smart_imputer = IterativeImputer(max_iter=10, random_state=0)

# Fit the machine learning model on training data and transform both sets
imputed_X_iter = pd.DataFrame(smart_imputer.fit_transform(X_train), index=X_train.index)
imputed_X_valid_iter = pd.DataFrame(smart_imputer.transform(X_valid), index=X_valid.index) # pyright: ignore[reportArgumentType]

# Copy the column names back (IterativeImputer removes them just like SimpleImputer)
imputed_X_iter.columns = X_train.columns
imputed_X_valid_iter.columns = X_valid.columns

# Print the final error score to compare with your other approaches
print("\nMAE from Approach 4 (Iterative Imputation):")
print(get_mae(imputed_X_iter, imputed_X_valid_iter, y_train, y_valid))