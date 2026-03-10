import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Open the multispectral image file
with rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/orthomosaic_0005set_sept_regular_ngl.tif') as src:
    green = src.read(2).astype(float)     # Green band (assuming band 2)
    red_edge = src.read(4).astype(float)  # Red Edge band (assuming band 4)
    nir = src.read(5).astype(float)       # NIR band (assuming band 5)
    transform = src.transform             # Get the transform
    crs = src.crs                        # Get the CRS (Coordinate Reference System)

# Handle potential zero values to avoid division by zero
green[green == 0] = np.nan
red_edge[red_edge == 0] = np.nan
nir[nir == 0] = np.nan

# Calculate the variant of MCARI
numerator = (nir - red_edge) - 0.2 * (nir - green)
denominator = nir / red_edge
mcari_variant = numerator / denominator

# Mask invalid values
mcari_variant = np.where(np.isnan(mcari_variant), -1, mcari_variant)
mcari_variant = np.clip(mcari_variant, -1, 1)  # Optional: clip values to the range [-1, 1]

# Plot the MCARI variant
plt.imshow(mcari_variant, cmap='RdYlGn', extent=(transform[2], transform[2] + transform[0] * mcari_variant.shape[1], 
                                                transform[5] + transform[4] * mcari_variant.shape[0], transform[5]))
plt.colorbar(label='MCARI')
plt.title('Modified Chlorophyll Absorption in Reflectance Index')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Save the MCARI variant image
with rasterio.open('mcari.tif', 'w', driver='GTiff', 
                   height=mcari_variant.shape[0], width=mcari_variant.shape[1], 
                   count=1, dtype=rasterio.float32, 
                   crs=crs, transform=transform) as dst:
    dst.write(mcari_variant.astype(rasterio.float32), 1)

