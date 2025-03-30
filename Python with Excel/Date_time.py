import pandas as pd
import seaborn as sns
from vega_datasets import local_data
import matplotlib as plt

seattle=local_data.seattle_weather()
print(seattle.head())

# Even though seattle_weather() comes from the vega_datasets library, the function itself returns a Pandas DataFrame
#
# The seattle variable is a Pandas DataFrame

date=pd.to_datetime('8th sep,2020 11:20 AM')
print(date)

print(date.hour)
print(date.minute)

print(seattle.dtypes)

print(seattle.head())
seattle['month_name']=seattle['date'].dt.month_name()
print(seattle['month_name'].head())
print(seattle['date'].max())

seattle_dates_changed=seattle['date'].dt.to_period('M')
print(seattle_dates_changed.head())

seattle.set_index(['date'],inplace=True)

# Sets the date column as the index of the DataFrame
#
# This makes date the primary reference point for accessing and analyzing data
#
# The inplace=True means the change is applied directly to seattle without creating a new copy

print(seattle['precipitation'].resample('W').sum())

# resample('W'): Groups the data into weekly intervals (W = Week)
#
# sum(): Computes the total precipitation for each week
