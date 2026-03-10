import pandas as pd
import numpy as np

# Load the original CSV file
df = pd.read_csv('csv_file')

# Number of synthetic rows to generate
num_new_rows = 1000

# Generate synthetic data using random noise around existing data
synthetic_rows = df.sample(n=num_new_rows, replace=True).copy()

# Add small noise to numeric columns
for col in df.select_dtypes(include=[np.number]).columns:
    noise = np.random.normal(0, 0.01 * df[col].std(), size=num_new_rows)
    synthetic_rows[col] += noise

# Combine original and synthetic data
augmented_df = pd.concat([df, synthetic_rows], ignore_index=True)

# Save the new dataset
augmented_df.to_csv('name_of_generated_file', index=False)
