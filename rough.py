import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"C:\Users\Sai Vijay Ragav\OneDrive\Documents\Programs\HeartAware\Amazon Sale Report.csv")

# Convert categorical columns to numerical (for chi-square)
for column in df.select_dtypes(include=['object']).columns:
    df[column] = LabelEncoder().fit_transform(df[column])

# Drop missing values
df = df.dropna()


group1 = df[df['Sales Channel '] == 1]['Amount']
group0 = df[df['Sales Channel '] == 0]['Amount']

t_stat, p_value_ttest = stats.ttest_ind(group1, group0, equal_var=False)  # Welch's T-test
print(f"T-Test: t-statistic = {t_stat}, p-value = {p_value_ttest}")

contingency_table = pd.crosstab(df['Sales Channel '], df['Amount'])
chi2_stat, p_value_chi2, _, _ = chi2_contingency(contingency_table)
print(f"Chi-Square Test: chi2-statistic = {chi2_stat}, p-value = {p_value_chi2}")
