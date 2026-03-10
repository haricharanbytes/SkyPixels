import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Open the multispectral image file
with rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/orthomosaic_0005set_sept_regular_ngl.tif') as src:
    blue = src.read(1).astype(float)  # Blue band
    red = src.read(3).astype(float)   # Red band
    nir = src.read(5).astype(float)   # NIR band
    transform = src.transform         # Get the transform
    crs = src.crs                     # Get the CRS (Coordinate Reference System)

# Handle potential zero values to avoid division by zero
blue[blue == 0] = np.nan
red[red == 0] = np.nan
nir[nir == 0] = np.nan

# EVI coefficients
G = 2.5
C1 = 6.0
C2 = 7.5
L = 1.0

# Calculate EVI
evi = G * (nir - red) / (nir + C1 * red - C2 * blue + L)

# Mask invalid values
evi = np.where(np.isnan(evi), -1, evi)
evi = np.clip(evi, -1, 1)  # Optional: clip values to the range [-1, 1]

# Plot the EVI
plt.imshow(evi, cmap='RdYlGn', extent=(transform[2], transform[2] + transform[0] * evi.shape[1], 
                                       transform[5] + transform[4] * evi.shape[0], transform[5]))
plt.colorbar(label='EVI')
plt.title('Enhanced Vegetation Index')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Save the EVI image
with rasterio.open('evi.tif', 'w', driver='GTiff', 
                   height=evi.shape[0], width=evi.shape[1], 
                   count=1, dtype=rasterio.float32, 
                   crs=crs, transform=transform) as dst:
    dst.write(evi.astype(rasterio.float32), 1)
