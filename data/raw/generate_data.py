"""
Sample Research Data Generator

This script generates synthetic data for the workshop template.
It creates realistic-looking research data for demonstration purposes.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of observations
n_obs = 500

# Generate sample data
data = {
    'id': range(1, n_obs + 1),
    'treatment': np.random.binomial(1, 0.5, n_obs),
    'age': np.random.normal(35, 10, n_obs).round(0).astype(int),
    'income': np.random.lognormal(10.5, 0.5, n_obs).round(2),
    'education_years': np.random.choice([12, 14, 16, 18, 20], n_obs, p=[0.2, 0.25, 0.3, 0.15, 0.1]),
    'outcome': np.random.normal(100, 15, n_obs).round(2),
}

# Add treatment effect
treatment_effect = 8
data['outcome'] = data['outcome'] + data['treatment'] * treatment_effect + np.random.normal(0, 5, n_obs)
data['outcome'] = data['outcome'].round(2)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure age is positive
df['age'] = df['age'].clip(lower=18, upper=80)

# Ensure income is positive
df['income'] = df['income'].clip(lower=5000)

# Save to CSV
df.to_csv('data/raw/sample_data.csv', index=False)

print(f"Generated {n_obs} observations")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nSummary statistics:")
print(df.describe())
print(f"\nData saved to data/raw/sample_data.csv")
