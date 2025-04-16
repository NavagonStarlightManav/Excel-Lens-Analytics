import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


data = {
    'Income': [417, 1250, 2083, 2917, 3750, 4583, 5417, 6250, 7083, 7917, 8750, 9583, 10417, 11250, 12500],
    'beach':  [5, 16, 19, 19, 25, 9, 14, 8, 7, 4, 3, 1, 1, 0, 3],
    'boat':   [9, 28, 45, 70, 62, 61, 37, 33, 26, 5, 11, 3, 3, 2, 23],
    'charter':[9, 39, 65, 100, 75, 53, 41, 26, 15, 11, 10, 3, 3, 0, 2],
    'pier':   [12, 23, 41, 33, 19, 18, 11, 8, 3, 1, 1, 4, 1, 0, 3]
}

df = pd.DataFrame(data)

long_df = pd.melt(df, id_vars='Income', var_name='activity', value_name='count')

expanded_rows = [
    {'Income': row['Income'], 'activity': row['activity']}
    for _, row in long_df.iterrows()
    for _ in range(int(row['count']))
]
expanded_df = pd.DataFrame(expanded_rows)

expanded_df['activity'] = expanded_df['activity'].astype('category')
expanded_df['activity'] = expanded_df['activity'].cat.reorder_categories(
    ['pier', 'beach', 'boat', 'charter'], ordered=True
)


X = expanded_df[['Income']]
X = sm.add_constant(X)
y = expanded_df['activity']


model = sm.MNLogit(y, X)
result = model.fit()


print(result.summary())

