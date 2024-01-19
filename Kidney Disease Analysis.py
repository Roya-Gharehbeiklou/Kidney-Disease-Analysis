import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import fsolve
from scipy.stats import norm
from sksurv.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from lifelines import KaplanMeierFitter, CoxPHFitter
import missingno as msno
import plotly.graph_objects as go

# Set the style for seaborn
sns.set(style='whitegrid')

# Function to calculate creatinine
def calculate_creatinine(row):
    kappa = 0.7 if row['sex'] == 0 else 0.9
    alpha = -0.329 if row['sex'] == 0 else -0.411
    min_val = lambda cr: (cr/kappa) if cr < kappa else 1
    max_val = lambda cr: (cr/kappa) if cr > kappa else 1

    def equation(cr):
        return row['egfr'] - (141 * min_val(cr)**alpha * max_val(cr)**-1.209 * 0.993**row['age'])

    cr_solution = fsolve(equation, 1)
    return cr_solution[0]

# Load dataset
df = pd.read_csv('data.csv')

# Calculate creatinine for each row
df['creatinine'] = df.apply(calculate_creatinine, axis=1)

# Define eGFR categories
conditions = [
    (df['egfr'] < 15),
    (df['egfr'] >= 60) & (df['egfr'] < 89),
    (df['egfr'] >= 30) & (df['egfr'] < 59),
    (df['egfr'] >= 15) & (df['egfr'] < 29),
    (df['egfr'] >= 90)
]
choices = ['Kidney Failure', 'Mildly reduced eGFR', 'Moderately reduced eGFR', 'Severely reduced eGFR', 'Normal']
df['eGFR_category'] = np.select(conditions, choices)

# Categorize kidney disease stage
def categorize_kidney_disease(creatinine):
    if creatinine < 1.5:
        return 'Stage 1'
    elif 1.5 <= creatinine < 2.0:
        return 'Stage 2'
    elif 2.0 <= creatinine < 5.0:
        return 'Stage 3'
    elif 5.0 <= creatinine < 8.0:
        return 'Stage 4'
    else:
        return 'Stage 5'

df['kidney_disease_stage'] = df['creatinine'].apply(categorize_kidney_disease)

# Save the updated DataFrame
df.to_csv('updated_dataset_with_stages.csv', index=False)

# Plotting
plt.figure(figsize=(10, 6))
df['kidney_disease_stage'].value_counts(normalize=True).sort_values().plot(kind='barh', color='yellowgreen')
plt.xlabel('Count (Percentage)')
plt.ylabel('Kidney Disease Stage')
plt.title('Count of Each Stage of Kidney Disease')
plt.grid(axis='x')
plt.show()
