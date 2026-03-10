import os
import rasterio

# Input orthomosaic.tif file path
input_path = 'orthomosaic_input_path'

# Output folder where individual bands will be saved
output_folder = 'output_path'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the orthomosaic.tif file
with rasterio.open(input_path) as src:
    # Loop through each band
    for band_idx in range(src.count):
        # Read the band data
        band = src.read(band_idx + 1)  # band_idx is 0-based index, +1 to access bands starting from 1

        # Get the band file name (e.g., orthomosaic_band1.tif, orthomosaic_band2.tif, ...)
        band_output_path = os.path.join(output_folder, f'orthomosaic_band{band_idx + 1}.tif')

        # Write the band data to a new GeoTIFF file
        with rasterio.open(band_output_path, 'w', driver='GTiff',
                           width=src.width, height=src.height,
                           count=1, dtype=src.dtypes[0],
                           crs=src.crs, transform=src.transform) as dst:
            dst.write(band, 1)

print("Band extraction completed.")