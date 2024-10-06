import pandas as pd
from scipy import stats

# Step 1: Load the dataset
df = pd.read_csv('data/marketing_data.csv')

# Step 2: Separate groups (A and B)
group_a = df[df['group_name'] == 'A']
group_b = df[df['group_name'] == 'B']

# Step 3: Perform t-test to compare conversion rates
t_stat, p_value = stats.ttest_ind(group_a['conversion'], group_b['conversion'])

# Step 4: Output the results
alpha = 0.05  # significance level

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis: The difference is statistically significant.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
