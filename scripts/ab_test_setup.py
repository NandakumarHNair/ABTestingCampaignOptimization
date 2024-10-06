import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv('data/marketing_data.csv')

# Step 2: Separate groups (A and B)
group_a = df[df['group_name'] == 'A']
group_b = df[df['group_name'] == 'B']

# Step 3: Calculate conversion rates
conv_rate_a = group_a['conversion'].mean()
conv_rate_b = group_b['conversion'].mean()

# Step 4: Visualize the conversion rates
labels = ['Group A', 'Group B']
rates = [conv_rate_a, conv_rate_b]

plt.bar(labels, rates, color=['blue', 'orange'])
plt.title('Conversion Rates by Group')
plt.ylabel('Conversion Rate')
plt.savefig('visualizations/ab_test_results.png')
plt.show()

# Print conversion rates
print(f"Group A Conversion Rate: {conv_rate_a:.2%}")
print(f"Group B Conversion Rate: {conv_rate_b:.2%}")
