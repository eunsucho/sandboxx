import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'Seoul_NC_pollen_data.csv'
df = pd.read_csv(file_path, encoding='euc-kr')  # Ensure encoding matches your file

# Select relevant columns
selected_columns = ['Date', 'Seoul_total', 'NC_total', 'S_trees', 'NC_trees']
fdf = df[selected_columns].copy()

# Convert 'Date' column to datetime
fdf['Date'] = pd.to_datetime(fdf['Date'], format='%m/%d/%Y')

# Interpolate missing values in NC_total and Seoul_total
fdf['NC_total'] = fdf['NC_total'].interpolate(method='linear')  # Interpolate missing values
fdf['Seoul_total'] = fdf['Seoul_total'].interpolate(method='linear')  # Interpolate missing values

# Define thresholds for pollen levels
pollen_level = {
    'low': 15,
    'moderate': 90,
    'high': 1500
}

# Filter data for the month of April
april_data = fdf[fdf['Date'].dt.month == 4]

# Plot daily pollen values for April with thresholds as background
def plot_april_pollen_with_thresholds():
    plt.figure(figsize=(12, 6))

    # Add background bands for thresholds
    max_value = april_data[['Seoul_total', 'NC_total']].max().max()
    plt.axhspan(0, pollen_level['low'], color='#A6D96A', alpha=0.3, label='Low')
    plt.axhspan(pollen_level['low'], pollen_level['moderate'], color='#FFFFBF', alpha=0.3, label='Moderate')
    plt.axhspan(pollen_level['moderate'], pollen_level['high'], color='#FDAE61', alpha=0.3, label='High')
    plt.axhspan(pollen_level['high'], max_value, color='#D7191C', alpha=0.3, label='Very High')

    # Plot daily pollen values for April
    plt.plot(april_data['Date'], april_data['Seoul_total'], label='Seoul', color='blue', marker='o')
    plt.plot(april_data['Date'], april_data['NC_total'], label='NC', color='orange', marker='o')

    # Add labels, legend, and title
    plt.xlabel('Date')
    plt.ylabel('Pollen Count')
    plt.title('Daily Pollen Levels in April with Thresholds')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig('pollen_plot_april.png', dpi=300, bbox_inches='tight')

    # Show the plot
    plt.show()

# Call the function to plot the graph for April and save it
plot_april_pollen_with_thresholds()