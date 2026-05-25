import pandas as pd

british_youtube = pd.read_csv('Pandas/Datasets/GBvideos.csv')
canadian_youtube = pd.read_csv('Pandas/Datasets/CAvideos.csv')

pd.concat([canadian_youtube, british_youtube])

# By default pandas performs a left join
# A left join combines two tables by keeping all records from the left table and only the matching records from the right table.

# setting the indexes
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left_joined_df = left.join(right, lsuffix='_CAN', rsuffix='_UK')
'''
Problem: Both datasets likely share identical column names, like views, likes, and dislikes. Pandas cannot have duplicate column names in one DataFrame.
Solution: The lsuffix and rsuffix parameters automatically rename overlapping columns.
Result: views becomes views_CAN for the Canadian data and views_UK for the UK data, allowing you to compare the stats side-by-side.
'''
# Display the first 5 rows
print(left_joined_df.head())
# joined_df.to_csv('youtube_trending_joined.csv')

# Right join
# It keeps all records from the right table (UK) and only includes matching data from the left table (Canada).
right_joined_df = left.join(right, lsuffix='_CAN', rsuffix='_UK', how='right') # rarely used

# Inner join
# An inner join is a method of combining two tables that keeps only the records that exist in both datasets
inner_joined_df = left.join(right, lsuffix='_CAN', rsuffix='_UK', how='inner')

# Outer join
# An outer join (or full outer join) combines two tables by keeping absolutely everything from both datasets.
outer_joined_df = left.join(right, lsuffix='_CAN', rsuffix='_UK', how='outer')
