import pandas as pd
from scipy.stats import f_oneway, shapiro
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Load the data from the CSV files
avl_file_path = 'sorted_avl.csv'  # Replace 'avl.csv' with the actual file path
gvl_file_path = 'sorted_gvl.csv'  # Replace 'gvl.csv' with the actual file path

avl_count_path ='avl_count.csv'
gvl_count_path ='gvl_count.csv'

# Load the datasets
avl_data = pd.read_csv(avl_file_path)
gvl_data = pd.read_csv(gvl_file_path)

avl_count = pd.read_csv(avl_count_path)
gvl_count = pd.read_csv(gvl_count_path)


# Assuming both datasets have a column named 'price'
avl_prices = avl_data['price']
gvl_prices = gvl_data['price']

avl_mean = avl_prices.mean()
gvl_mean = gvl_prices.mean()

avl_std = np.std(avl_prices)
gvl_std = np.std(gvl_prices)

# Perform ANOVA
avl_shap,temp = shapiro(avl_prices)
gvl_shap,temp = shapiro(gvl_prices)

f_statistic, p_value = f_oneway(avl_prices, gvl_prices)
all_prices = np.concatenate([avl_prices, gvl_prices])

# Calculate Grand Mean
grand_mean = (avl_mean + gvl_mean) / 2

# Calculate Sum of Squares Total (SST)
sst = np.sum((all_prices - grand_mean)**2)

# Calculate Sum of Squares Between (SSB)
ssb = len(avl_prices) * (avl_mean - grand_mean)**2 + len(gvl_prices) * (gvl_mean
 - grand_mean)**2

# Calculate Sum of Squares Within (SSW)
ssw = sst - ssb

# Degrees of Freedom
df_between = 2 - 1  # Number of groups - 1
df_within = len(all_prices) - 2  # Total number of observations - Number of groups

# Mean Squares
ms_between = ssb / df_between
ms_within = ssw / df_within

# Print results
print(f'Asheville Mean: {avl_mean:.2f}')
print(f'Greenville Mean: {gvl_mean:.2f}')
print(f'Asheville Standard Deviation: {avl_std:.2f}')
print(f'Greenville Standard Deviation: {gvl_std:.2f}')
print(f'Grand Mean: {grand_mean:.2f}')
print(f'SST: {sst:.2f}')
print(f'SSB: {ssb:.2f}')
print(f'SSW: {ssw:.2f}')
print(f'MS Between: {ms_between:.2f}')
print(f'MS Within: {ms_within:.2f}')
print(f'DF Between: {df_between}')
print(f'DF Within: {df_within}')
print(f"Shapiro-Wilk Test for Asheville: {avl_shap}")
print(f"Shapiro-Wilk Test for Greenville: {gvl_shap}")
print(f'F-statistic: {f_statistic:.2f}')
print(f'P-value: {p_value:.2f}')

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in prices.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in prices.")





data = pd.DataFrame({'Prices': np.concatenate([avl_prices, gvl_prices]),
                     'City': np.repeat(['Asheville', 'Greenville'], [len(avl_prices), len(gvl_prices)])})
# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='City', y='Prices', data=data, color="slategray")
plt.title('Distribution of Prices Between Asheville and Greenville')
plt.xlabel('City')
plt.ylabel('Prices')
plt.axhline(np.mean(avl_prices), color='skyblue', linestyle='solid', linewidth=2, label='Asheville Mean')
plt.axhline(np.mean(gvl_prices), color='gold', linestyle='solid', linewidth=2, label='Greenville Mean')

plt.figure(figsize=(10,6))
plt.scatter(avl_data.index, avl_prices, color="cornflowerblue", label="Asheville Prices")
plt.title('Price Curve Sorted by Price')
plt.scatter(gvl_data.index, gvl_prices, color="darkolivegreen", label="Greenville Prices")
plt.xlabel('Index')
plt.ylabel('Price')

plt.figure(figsize=(10,6))
plt.title('Distributions of Price within Greenville and Asheville')
plt.plot(avl_count['Range'],avl_count['Occurences'], color="cornflowerblue", label="Asheville Distribution")
plt.plot(gvl_count['Range'],gvl_count['Occurences'], color="darkolivegreen", label="Greenville Distribution")
plt.xlabel('Range')
plt.ylabel('Count')

plt.legend()
plt.show()