import pandas as pd
import os

# Load the CSV file
file_path = 'csv_file'
data = pd.read_csv(file_path)

# Fill NaN values using interpolation
data_interpolated = data.interpolate(method='linear', limit_direction='forward', axis=0)

# Save the interpolated dataset to a new CSV file
filename = os.path.splitext(file_path)[0]
output_file_path = f'{filename}_interpolated.csv'
data_interpolated.to_csv(output_file_path, index=False)


print("Interpolated dataset saved to:", output_file_path)