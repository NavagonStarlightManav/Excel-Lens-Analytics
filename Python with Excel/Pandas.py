import pandas as pd
import openpyxl

orders=pd.read_excel("superstore.xlsx",sheet_name="returns")
print(orders.head())

returns=pd.read_excel("superstore.xlsx",sheet_name="orders")
print(returns.head())

returns=pd.read_excel("superstore.xlsx",sheet_name='returns',names=['returned','details'])
print(returns.head())

returns.to_excel('Returns.xlsx',index=False)


