import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set a clean visual style for all plots
sns.set_theme(style="whitegrid")

np.random.seed(42)
data = pd.DataFrame({
    'Age': np.random.normal(loc=35, scale=10, size=200).astype(int),
    'Blood_Pressure': np.random.normal(loc=120, scale=15, size=200).astype(int),
    'Date': pd.date_range(start="2026-01-01", periods=200, freq='D'),
    'Stock_Price': 100 + np.cumsum(np.random.normal(0, 2, size=200))
})

# Add manual outliers to Blood Pressure for the boxplot example
data.loc[:5, 'Blood_Pressure'] = [190, 195, 200, 60, 55, 50] # changes the first 6 values to the following in the Blood_Pressure column
# Histogram
# Histogram with a Kernel Density Estimate (KDE) line overlaid
plt.figure(figsize=(10, 5)) # Determines the size of the figure
sns.histplot(data=data, x='Age', kde=True, color='skyblue')
plt.title('Data Distribution & Spread (Age)')
plt.xlabel('Age')
plt.ylabel('Count / Density')
plt.show()

# Kernel Density Estimate Line
sns.kdeplot(data=data, x='Age', color='skyblue', fill = True) # 'fill'(previously called shade) colors the area below the curve
plt.title('Kernel Density Estimate line')
plt.show()

# 2D Kernel Density Estimate Line
iris_data = sns.load_dataset("iris")
sns.jointplot(data, x='Age', y='Blood_Pressure', kind="kde", cmap = 'viridis')
# It gives you three charts at once (the 2D map in the middle plus the 1D charts on the sides) so you can see everything in one click.
# good for analysing data
plt.show()

# Same but cleaner, removes the 1D charts
# good for presentation or reports
sns.kdeplot(
    data=iris_data, 
    x="petal_length", 
    y="sepal_width", 
    hue="species",   # Splits data by category
    fill=True, 
    alpha=0.5        # Makes the overlapping shapes transparent
)
# It gives you just the clean 2D map, which is much easier to resize, move around, or fit into a slide layout next to other charts.
plt.show()

# Box Plot
# Boxplot displays median, quartiles, and whiskers. Dots represent outliers.
# We have already set outliers manually
plt.figure(figsize=(10, 4))
sns.boxplot(data=data, x='Blood_Pressure', color='lightgreen')
plt.title('Outliers & Ranges (Blood Pressure)')
plt.xlabel('Blood Pressure (mmHg)')
plt.show()

# Scatter Plot
# Scatterplots map individual data points on X and Y grids to show correlation.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Age', y='Blood_Pressure', color='coral', alpha=0.8)
plt.title('Relationships & Correlations (Age vs. Blood Pressure)')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.show()
print(data.corr)

# Line Plot
# Line plots connect sequential data points, perfect for time-series analysis.
plt.figure(figsize=(12, 5))
sns.lineplot(data=data, x='Date', y='Stock_Price', color='purple', linewidth=2)
plt.title('Trends Over Time (Stock Price Progression)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)  # Clean up date label spacing
plt.tight_layout()
plt.show()


df = pd.DataFrame({
    "X_Num": [10, 20, 30, 40],
    "Y_Num": [1.5, 3.8, 2.4, 5.1],
    "Group": ["A", "A", "B", "B"]
})

# You can use sns.displot() to plot histogram, ecdfs and KDE graphs
# To plot use the kind arguement: kde, hist, ecdf
# you can also plot 2 types of graphs on 1
# by using sns.displot(hist=True) or sns.displot(kde=True)
sns.displot(df, kind = 'hist', kde=True)
plt.title('Distribution Plot')
plt.show()

# You can use sns.relplot() to plot line and scatter
# to plot use the kind arguement: scatter, line
sns.relplot(df, kind = 'line')
plt.title('Relational Plot')
plt.show()

# You can use sns.catplot() to plot a lot many categories of graphs
# the main ones are bar, box, violin
# using the kind arguement: bar, box, violin
sns.catplot(df, kind = 'bar')
plt.title('Categorical Plot')
plt.show()

# Overlaid Representations
# Combine a histogram, smooth line, and raw data ticks all at once
# What rug does: Draws tiny, fine vertical tick marks along the bottom X-axis.
sns.displot(data=df, kind='hist', kde=True, rug=True)
plt.show()

# Hue Grouping
# Compare age distributions between genders on the exact same axis
# Keeps everything on a single chart but colors the data points differently based on their category.
sns.relplot(data=df, x='X_Num', y = 'Y_Num', kind='scatter', hue='Group')
plt.title('Hue Grouping')
plt.show()


# Heatmap
# Heatmap showing average arrival delay for each airline by month
plt.figure(figsize=(14,7))
plt.title("Average Arrival Delay for Each Airline, by Month")
sns.heatmap(data=df.select_dtypes(include=np.number), annot=True)
plt.xlabel("Airline")
plt.show()

# Regression Plot
# Plotting a Line of Best Line(Regression Line)
# It also shades the confidence interval
# What the Confidence Interval is
'''Think of the 95% confidence interval as a "safety zone" for the line of best fit.
If you collected a brand new batch of data from the exact same source tomorrow, the new line of best fit would almost certainly change slightly.
The shaded band shows you the area where that new line is 95% likely to fall.
By default, sns.regplot() displays a 95% confidence interval.'''
# You can manually set the confidence interval
# by using the ci arguement 'ci = 99' you can set the confidence interval to 99%
# or you can completely remove it by using ci = None
sns.regplot(df, x = 'X_Num', y = 'Y_Num', ci = None)
plt.show()

# Linear Model Plot
# sns.lmplot() is a figure-level function in Seaborn used to plot lines of best fit across different categories of your data.
# You can automatically draw separate lines of best fit for different categories on the exact same graph.
sns.lmplot(df, x = 'X_Num', y = 'Y_Num', ci = None)
plt.show()

sns.lmplot(data=df, x="X_Num", y="Y_Num", col="Group")
# col splits the A and B graphs seperately vertically, one graph only having A values and one graph with only having B values
sns.lmplot(data=df, x="X_Num", y="Y_Num", row="Group")
# row splits the A and B graphs seperately horizontal, one graph only having A values and one graph with only B values
plt.show()