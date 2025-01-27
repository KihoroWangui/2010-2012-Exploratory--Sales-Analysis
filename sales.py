import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading datasets
sales = pd.read_csv('sales data-set.csv')  
features = pd.read_csv('Features data set.csv')  
stores = pd.read_csv('stores data-set.csv') 

# Preview data
print(sales.head())
print(features.head())
print(stores.head())
# missing values
print(sales.isnull().sum())
print(features.isnull().sum())
print(stores.isnull().sum())

#Filling missing values
features.fillna({'Markdown': 0}, inplace=True)

#checking datatypes
print(sales.info())
print(features.info())
print(stores.info())

# dataset merging
sales_features = pd.merge(sales, features, on=['Store', 'Date'], how='inner')
final_data = pd.merge(sales_features, stores, on='Store', how='inner')

print(final_data.head())
#KPI Calculation
#total sales
total_sales = final_data['Weekly_Sales'].sum()
print(f"Total Sales: {total_sales}")
#average sales per store
average_sales_store = final_data.groupby('Store')['Weekly_Sales'].mean()
print(average_sales_store)
#best performing store
top_stores = final_data.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False)
print(top_stores.head())
#sales during markdowns
sales_during_markdowns = final_data[final_data['MarkDown4'] > 0].groupby('Store')['Weekly_Sales'].sum()
print(sales_during_markdowns)
#correlation between sales and fuel price
correlation = final_data['Fuel_Price'].corr(final_data['Weekly_Sales'])
print(f"Correlation between Fuel Price and Sales: {correlation}")

#visualization 
# of sales over time
plt.figure(figsize=(10, 6))
sales_trends = final_data.groupby('Date')['Weekly_Sales'].sum()
plt.plot(sales_trends.index, sales_trends.values)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly_Sales')
plt.grid()
plt.show()
#top 10 stores based on sales
top_stores.head(10).plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Stores by Total Sales')
plt.xlabel('Store')
plt.ylabel('Total Sales')
plt.show()
#markdown effect on sales
plt.figure(figsize=(10, 6))
sns.boxplot(x='MarkDown4', y='Weekly_Sales', data=final_data)
plt.title('Effect of Markdowns on Sales')
plt.show()
#fuel prices against sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Fuel_Price', y='Weekly_Sales', data=final_data)
plt.title('Fuel Price vs. Sales')
plt.show()
#export data
final_data.to_csv('final_data_analysis.csv', index=False)
top_stores.to_csv('top_stores.csv', index=False)









