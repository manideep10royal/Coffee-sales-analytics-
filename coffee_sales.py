import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==================== 1. DATA LOADING ====================
print("="*60)
print("COFFEE SALES DATA SCIENCE ANALYSIS")
print("="*60)

data_dir = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(data_dir, 'index (2).csv'))

# ==================== 2. EXPLORATORY DATA ANALYSIS ====================
print("\n📊 DATASET OVERVIEW")
print("-" * 60)
print(f"Dataset Shape: {data.shape[0]} rows, {data.shape[1]} columns")
print("\nFirst 5 rows:")
print(data.head())

print("\nData Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nBasic Statistics:")
print(data.describe())

# ==================== 3. DATA CLEANING ====================
print("\n🔧 DATA CLEANING")
print("-" * 60)
# Convert datetime column
data['datetime'] = pd.to_datetime(data['datetime'])
data['date'] = pd.to_datetime(data['date'])

# Extract useful time features
data['hour'] = data['datetime'].dt.hour
data['day'] = data['datetime'].dt.day
data['month'] = data['datetime'].dt.month
data['day_of_week'] = data['datetime'].dt.day_name()
data['week_of_year'] = data['datetime'].dt.isocalendar().week

print("✓ DateTime features extracted")
print(f"✓ Data type conversions completed")

# ==================== 4. STATISTICAL ANALYSIS ====================
print("\n📈 KEY INSIGHTS")
print("-" * 60)

# Total sales
total_sales = data['money'].sum()
print(f"Total Sales Revenue: ${total_sales:,.2f}")

# Average sale
avg_sale = data['money'].mean()
print(f"Average Transaction Value: ${avg_sale:.2f}")

# Most popular coffee
most_popular = data['coffee_name'].value_counts()
print(f"\nTop 5 Most Popular Drinks:")
print(most_popular.head())

# Sales by hour
print(f"\nPeak Sales Hour:")
hourly_sales = data.groupby('hour')['money'].agg(['sum', 'count'])
peak_hour = hourly_sales['sum'].idxmax()
print(f"Hour {peak_hour}:00 - ${hourly_sales.loc[peak_hour, 'sum']:.2f} ({int(hourly_sales.loc[peak_hour, 'count'])} transactions)")

# Sales by day of week
print(f"\nSales by Day of Week:")
daily_sales = data.groupby('day_of_week')['money'].sum().sort_values(ascending=False)
print(daily_sales)

# ==================== 5. DATA VISUALIZATION ====================
print("\n📊 GENERATING VISUALIZATIONS")
print("-" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Coffee Sales Analysis Dashboard', fontsize=16, fontweight='bold')

# Plot 1: Sales by Coffee Type
ax1 = axes[0, 0]
most_popular.head(10).plot(kind='barh', ax=ax1, color='#8B4513')
ax1.set_title('Top 10 Coffee Types Sold')
ax1.set_xlabel('Number of Transactions')

# Plot 2: Hourly Sales Distribution
ax2 = axes[0, 1]
hourly_sales['sum'].plot(kind='bar', ax=ax2, color='#D2691E')
ax2.set_title('Sales Revenue by Hour')
ax2.set_xlabel('Hour of Day')
ax2.set_ylabel('Revenue ($)')
ax2.tick_params(axis='x', rotation=45)

# Plot 3: Daily Sales Trend
ax3 = axes[1, 0]
daily_trend = data.groupby('date')['money'].sum().sort_index()
ax3.plot(daily_trend.index, daily_trend.values, linewidth=2, color='#CD853F')
ax3.set_title('Daily Sales Trend')
ax3.set_xlabel('Date')
ax3.set_ylabel('Revenue ($)')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(True, alpha=0.3)

# Plot 4: Price Distribution by Coffee Type
ax4 = axes[1, 1]
data.boxplot(column='money', by='coffee_name', ax=ax4)
ax4.set_title('Price Distribution by Coffee Type')
ax4.set_xlabel('Coffee Type')
ax4.set_ylabel('Price ($)')
plt.suptitle('')  # Remove the automatic title from boxplot
ax4.tick_params(axis='x', rotation=45)

plt.tight_layout()
output_path = os.path.join(data_dir, 'coffee_sales_analysis.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Dashboard saved to: {output_path}")

# ==================== 6. SUMMARY ====================
print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
print(f"📁 Visualization saved: coffee_sales_analysis.png")
print(f"📋 Total transactions analyzed: {len(data)}")
print(f"💰 Total revenue: ${total_sales:,.2f}")
print("="*60)
