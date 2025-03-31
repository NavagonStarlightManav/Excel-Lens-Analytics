import pandas as pd
import seaborn as sns
import jinja2

tips=sns.load_dataset('tips')
print(tips.head())

def highlight_cells(value):
    color='orange' if value>3 else ""
    return 'background-color: {}'.format(color)

print(tips.style.map(highlight_cells,subset=pd.IndexSlice[:,['tip']])) # The style property only works in environments that support HTML rendering, such as Jupyter Notebook

# Now we will create a function that will loop down every row of tip column and apply conditional formatting to whole row

def highlight_rows(row):
    value = row['tip']  # Access the 'tip' column directly
    if value > 5:
        color = '#90ee90'  # Light green for tips > 5
    elif value > 3:
        color = '#ffffe0'  # Light yellow for tips > 3 and <= 5
    else:
        color = '#ffffff'  # White for tips <= 3
    return ['background-color: {}'.format(color) for r in row] # after a particular condiition has been met , we loop through all columns of that row to apply colour]

# Apply the styling to the DataFrame
tips.style.apply(highlight_rows, axis=1).to_excel('style.xlsx',engine='openpyxl') # This also will work in jupyter notebook