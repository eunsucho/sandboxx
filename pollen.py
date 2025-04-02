import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Seoul_NC_pollen_data.csv'
df = pd.read_csv(file_path, encoding='euc-kr')  # Ensure encoding matches your file

# Select relevant columns
selected_columns = ['Date', 'S_trees', 'NC_trees']
fdf = df[selected_columns].copy()

# Convert 'Date' column to datetime
fdf['Date'] = pd.to_datetime(fdf['Date'], format='%m/%d/%Y')

fdf['NC_total'].fillna(0, )
fdf['Seoul_total'].fillna(0) # Fill NaN values with 0

# Define thresholds for pollen levels
pollen_level = {
    'low': 15,
    'moderate': 90,
    'high': 1500
}

# Plot daily pollen values with thresholds as background
def plot_pollen_with_thresholds():
    plt.figure(figsize=(12, 6))

    # Add background bands for thresholds
    plt.axhspan(0, pollen_level['low'], color='#A6D96A', alpha=0.3, label='Low')
    plt.axhspan(pollen_level['low'], pollen_level['moderate'], color='#FFFFBF', alpha=0.3, label='Moderate')
    plt.axhspan(pollen_level['moderate'], pollen_level['high'], color='#FDAE61', alpha=0.3, label='High')
    plt.axhspan(pollen_level['high'], fdf[['Seoul_total', 'NC_total']].max().max(), color='#D7191C', alpha=0.3, label='Very High')

    # Plot daily pollen values
    plt.plot(fdf['Date'], fdf['Seoul_total'], label='Seoul', color='blue', marker='o')
    plt.plot(fdf['Date'], fdf['NC_total'], label='NC', color='orange', marker='o')

    # Add labels, legend, and title
    plt.xlabel('Date')
    plt.ylabel('Pollen Count')
    plt.title('Daily Pollen Levels with Thresholds')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Call the function to plot the graph
plot_pollen_with_thresholds()

plt.savefig('pollen_plot.png', dpi=300)
plt.show()