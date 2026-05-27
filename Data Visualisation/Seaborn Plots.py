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
plt.figure(figsize=(10, 5)) # Determines the size of the figure
# Histogram
# Histogram with a Kernel Density Estimate (KDE) line overlaid
sns.histplot(data=data, x='Age', kde=True, color='skyblue')
plt.title('Data Distribution & Spread (Age)')
plt.xlabel('Age')
plt.ylabel('Count / Density')
plt.show()

# Kernel Density Estimate Line
sns.kdeplot(data=data, x='Age', color='skyblue')
plt.show()



plt.figure(figsize=(10, 4))
# Box Plot
# Boxplot displays median, quartiles, and whiskers. Dots represent outliers.
# We have already set outliers manually
sns.boxplot(data=data, x='Blood_Pressure', color='lightgreen')
plt.title('Outliers & Ranges (Blood Pressure)')
plt.xlabel('Blood Pressure (mmHg)')
plt.show()



plt.figure(figsize=(10, 6))
# Scatter Plot
# Scatterplots map individual data points on X and Y grids to show correlation.
sns.scatterplot(data=data, x='Age', y='Blood_Pressure', color='coral', alpha=0.8)
plt.title('Relationships & Correlations (Age vs. Blood Pressure)')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.show()
print(data.corr)


plt.figure(figsize=(12, 5))
# Line Plot
# Line plots connect sequential data points, perfect for time-series analysis.
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

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=df.select_dtypes(include=np.number), annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")
plt.show()

# Plotting a Line of Best Line(Regression Line)
sns.regplot(df, x = 'X_Num', y = 'Y_Num')
plt.show()