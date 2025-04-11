import pandas as pd
import openpyxl as ps
import statsmodels.api as sm

# File path
file_path = r"C:\Users\manav\Desktop\Career_Essentials\Machine_Learning_Analysis\Binomial Excel Solver.xlsx"

df = pd.read_excel(file_path, sheet_name='Logistic X1 (MLE)',header=4)  # replace 'Sheet1' with the actual sheet name


X = df[['X1']]
y = df['y']

X = sm.add_constant(X)

model = sm.GLM(y, X, family=sm.families.Binomial())
result = model.fit()

print(result.summary())


