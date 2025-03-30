import pandas as pd
import seaborn as sns

tips =sns.load_dataset('tips')
print(tips.head())

tips['tips_pct']=tips['tip']/tips['total_bill']
tips['tips_pct']=tips['tips_pct'].round(2)
print(tips.head())

tips.drop('tips_pct',axis='columns',inplace=True)
print(tips.columns)


dinner=tips.query('time=="Dinner"')
print(dinner.head())

dinner_sorted=dinner.sort_values(by="total_bill",ascending=False)
print(dinner_sorted.head())