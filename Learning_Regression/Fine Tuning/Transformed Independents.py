import numpy as np
import pandas as pd
import openpyxl as ps
import statsmodels.api as sm


file_path = r"C:\Users\manav\Desktop\Career_Essentials\Machine_Learning_Analysis\Multiple_Independent_variables.xlsx"

df = pd.read_excel(file_path, sheet_name='Transformed Independents',header=1)  # replace 'Sheet1' with the actual sheet name


X = df[['Transform(X1)','X2','X3']]
y = df['y']

X = sm.add_constant(X)

model = sm.GLM(y, X, family=sm.families.Binomial())


result = model.fit()


# df['logit'] = result.fittedvalues
# This is not true logit

df['logit'] = result.params['const'] + result.params['Transform(X1)'] * df['X1']


df['odds'] = df['logit'].apply(lambda x: np.exp(-1*x))


df['predicted_probability'] = result.predict(X)

print(result.summary())

print(df[['logit', 'odds', 'predicted_probability']].head())

import matplotlib.pyplot as plt

# Scatter: Actual outcomes
plt.figure(figsize=(10, 6))
plt.scatter(df['X1'], df['y'], color='blue', alpha=0.5, label='Actual Outcomes (y)')

# Curve: Predicted sigmoid probabilities
# Sort values for a smooth curve
sorted_df = df.sort_values(by='X1')
plt.plot(sorted_df['X1'], sorted_df['predicted_probability'], color='red', linewidth=2, label='Predicted Probability (Sigmoid Curve)')

# Axis Labels
plt.xlabel('Points Scored (X1) →')
plt.ylabel('Outcome →\n0 = Loss, 1 = Win')
plt.title('Logistic Regression: Actual Outcomes vs Predicted Probabilities')
plt.legend()

# Annotate Y-axis
plt.text(df['X1'].min() - 5, 1, 'Actual Outcome: Win (1)', fontsize=10, color='blue')
plt.text(df['X1'].min() - 5, 0, 'Actual Outcome: Loss (0)', fontsize=10, color='blue')

# Annotate X-axis
plt.text(df['X1'].mean(), -0.1, 'X1: Points Scored', ha='center', fontsize=10, color='black')

plt.grid(True)
plt.ylim(-0.1, 1.1)
plt.show()






