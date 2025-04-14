import numpy as np
import pandas as pd
import openpyxl as ps
import statsmodels.api as sm
import pandas as pd


file_path = r"C:\Users\manav\Desktop\Career_Essentials\Machine_Learning_Analysis\confusion matrix.xlsx"

df = pd.read_excel(file_path, sheet_name='Logistic X1+X2+X2 Confusion',header=1)  # replace 'Sheet1' with the actual sheet name


X = df[['X1','X2','X3']]
y = df['y']

X = sm.add_constant(X)

model = sm.GLM(y, X, family=sm.families.Binomial())


result = model.fit()


# df['logit'] = result.fittedvalues
# This is not true logit

df['logit'] = result.params['const'] + result.params['X1'] * df['X1']


df['odds'] = df['logit'].apply(lambda x: np.exp(-1*x))


df['predicted_probability'] = result.predict(X)

print(result.summary())

print(df[['logit', 'odds', 'predicted_probability']].head())

from sklearn.metrics import confusion_matrix

# Step 1: Predict classes (0 or 1)
predicted_classes = [1 if p >= 0.5 else 0 for p in df['predicted_probability']]

# Step 2: Create confusion matrix
cm = confusion_matrix(df['y'], predicted_classes)

# Step 3: Print matrix
print("Confusion Matrix:")
print(cm)

# Actual and predicted labels (example matching your matrix)
y_true = [0]*31 + [1]*36  # 31 actual 0s, 36 actual 1s
y_pred = [0]*23 + [1]*8 + [0]*10 + [1]*26  # From confusion matrix: [[23, 8], [10, 26]]

# Get the confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Convert to relative frequencies
rel = cm / cm.sum()

# Convert to DataFrame
df = pd.DataFrame({
    'Var1': [0, 1, 0, 1],
    'Var2': [0, 0, 1, 1],
    'Freq': [rel[0, 0], rel[1, 0], rel[0, 1], rel[1, 1]]
})

print(df)

