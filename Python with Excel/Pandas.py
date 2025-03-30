import pandas as pd
import openpyxl

orders=pd.read_excel("superstore.xlsx",sheet_name="returns")
print(orders.head())

returns=pd.read_excel("superstore.xlsx",sheet_name="orders")
print(returns.head())

returns=pd.read_excel("superstore.xlsx",sheet_name='returns',names=['returned','details'])
print(returns.head())

returns.to_excel('Returns.xlsx',index=False)


df = pd.read_csv('file.txt', delimiter='\t')
print(df.head())

# Pandas does not have a read_text() function because text files can have different structures (e.g., CSV, JSON, XML, etc.)
# Instead, Pandas provides specific functions like read_csv(), read_json(), read_excel(), etc., to handle different data formats

