import pandas as pd

# 1. Create a raw dataset from scratch
data = {
    'country': ['US', 'US', 'Argentina', 'Greece', 'Argentina', 'US'],
    'province': ['California', 'Texas', 'Mendoza', 'Sterea Ellada', 'Mendoza', 'California'],
    'winery': ['Winery A', 'Winery B', 'Winery C', 'Winery D', 'Winery E', 'Winery F']
}
df = pd.DataFrame(data)
print("--- 1. Raw DataFrame ---")
print(df, "\n")

# 2. Group by multiple columns to automatically create a MultiIndex
# This counts the number of wineries per country and province
countries_reviewed = df.groupby(['country', 'province']).size().to_frame(name='len')
#.size(): It counts how many rows fell into each group. This creates a pandas Series.
#.to_frame(name='len'): It converts that Series back into a nice tabular DataFrame and names the new count column 'len'.
# Because we grouped by two items, this step automatically generates the MultiIndex.
print("--- 2. DataFrame with a MultiIndex (Notice the nested row labels) ---")
print(countries_reviewed, "\n")

# 3. Flatten the MultiIndex into regular columns
countries_reviewed = countries_reviewed.reset_index()#  Fixing and Flattening the Layout
print("--- 3. Flattened DataFrame (After reset_index) ---")
print(countries_reviewed, "\n")

# 4. Sort the DataFrame by the 'len' column in descending order
countries_reviewed_sorted = countries_reviewed.sort_values(by='len', ascending=False) # Sorting the Results
print("--- 4. Final Sorted DataFrame ---")
print(countries_reviewed_sorted)
