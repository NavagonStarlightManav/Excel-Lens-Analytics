import pandas as pd
import seaborn as sns
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import BarChart, Series, Reference

nyc = pd.read_excel('nyc-pop.xlsx')


print(nyc.head())

nyc.sort_values(by='pop',ascending=False,inplace=True)
wb=openpyxl.Workbook()
ws=wb.active

for r in dataframe_to_rows(nyc,index=False,header=True):
    ws.append(r)

pop_col = nyc.columns.get_loc('pop') + 1
print(pop_col)

# Get the column index of 'borough' and add 1
borough_col = nyc.columns.get_loc('borough') + 1
print(borough_col)

# Get the number of rows in 'nyc' and add 1
max_row = nyc.shape[0] + 1

# Create a BarChart object
chart1 = BarChart()

# Define the data range for the chart
data = Reference(ws, min_col=pop_col, min_row=1, max_row=max_row)

# Define the categories (x-axis) for the chart
cats = Reference(ws, min_col=borough_col, min_row=2, max_row=max_row)

# Add the data to the chart with titles from the data range
chart1.add_data(data, titles_from_data=True)

# Set the categories for the chart
chart1.set_categories(cats)

# Set the title of the chart
chart1.title = 'NYC population by borough'

# Add the chart to the worksheet at cell 'A10'
ws.add_chart(chart1, 'A10')

# Save the workbook with the chart
wb.save('nyc-pop-chart.xlsx')