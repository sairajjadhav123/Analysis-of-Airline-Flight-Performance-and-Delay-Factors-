# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Replace this with the actual path to your CSV file
file_path = '/Users/sairajjadhav/Desktop/airline_cleaned_csv_new.csv'

# Load the data
df = pd.read_csv(file_path)

# Drop rows with NaN or inf values in 'DepDelayMinutes' or 'ArrDelayMinutes'
df = df.dropna(subset=['DepDelayMinutes', 'ArrDelayMinutes'])

# Calculate the correlation
correlation, _ = pearsonr(df['DepDelayMinutes'], df['ArrDelayMinutes'])
print('Pearson correlation:', correlation)

# Group by the 'Reporting_Airline' and calculate mean delays
# Note that newer versions of pandas require you to use named aggregation
airline_performance = df.groupby('Reporting_Airline').agg(
    MeanDepDelay=pd.NamedAgg(column='DepDelayMinutes', aggfunc='mean'),
    MeanArrDelay=pd.NamedAgg(column='ArrDelayMinutes', aggfunc='mean')
)

# Add a new column for the sum of mean delays
airline_performance['TotalDelay'] = airline_performance['MeanDepDelay'] + airline_performance['MeanArrDelay']

# Sort airlines by the total mean delay to find the best and worst on-time performance
best_performance = airline_performance.sort_values('TotalDelay')
worst_performance = airline_performance.sort_values('TotalDelay', ascending=False)

print('Best On-Time Performance Airlines:\n', best_performance.head())
print('Worst On-Time Performance Airlines:\n', worst_performance.head())


import matplotlib.pyplot as plt

# Histogram for departure delays
plt.figure(figsize=(10, 6))
plt.hist(df['DepDelayMinutes'].dropna(), bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Departure Delays')
plt.xlabel('Delay (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram for arrival delays
plt.figure(figsize=(10, 6))
plt.hist(df['ArrDelayMinutes'].dropna(), bins=50, color='salmon', edgecolor='black')
plt.title('Distribution of Arrival Delays')
plt.xlabel('Delay (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Box plot for departure and arrival delays
plt.figure(figsize=(12, 7))
df.boxplot(column=['DepDelayMinutes', 'ArrDelayMinutes'])
plt.title('Box Plot of Departure and Arrival Delays')
plt.ylabel('Delay (minutes)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['DepDelayMinutes'], df['ArrDelayMinutes'], alpha=0.5)
plt.title('Scatter Plot of Departure vs. Arrival Delays')
plt.xlabel('Departure Delay (minutes)')
plt.ylabel('Arrival Delay (minutes)')
plt.grid(True)
plt.show()


# Bar chart for best on-time performance airlines
best_performance['TotalDelay'].plot(kind='bar', figsize=(10, 6), color='green')
plt.title('Best On-Time Performance Airlines')
plt.xlabel('Airline')
plt.ylabel('Average Total Delay (minutes)')
plt.show()

# Bar chart for worst on-time performance airlines
worst_performance['TotalDelay'].plot(kind='bar', figsize=(10, 6), color='red')
plt.title('Worst On-Time Performance Airlines')
plt.xlabel('Airline')
plt.ylabel('Average Total Delay (minutes)')
plt.show()

#