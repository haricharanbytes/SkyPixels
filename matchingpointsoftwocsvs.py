import pandas as pd

# Read both CSV files
def find_matching_points(file1_path, file2_path):
    """
    Find matching latitude and longitude points between two CSV files.
    """
    try:
        # Read the files
        df1 = pd.read_csv('hpt_sep2024.csv')
        df2 = pd.read_csv('gcvi_hpt_sep24.csv')
        
        # Print the column names to help with debugging
        print("File 1 columns:", df1.columns.tolist())
        print("File 2 columns:", df2.columns.tolist())
        
        # Merge the dataframes on latitude and longitude
        merged_df = pd.merge(df1, df2, 
                           on=['Latitude', 'Longitude'],
                           how='inner',
                           suffixes=('_file1', '_file2'))
        
        print(f"Found {len(merged_df)} matching points")
        return merged_df
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

matched_points = find_matching_points('your_first_file.csv', 'your_second_file.csv')
if matched_points is not None:
    matched_points.to_csv('matching_points.csv', index=False)