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



# Export KPIs and summarized data
final_data.to_excel('final_data_analysis.csv', index=False)

# Save specific results, e.g., top-performing stores
top_stores.to_excel('top_stores.csv')









