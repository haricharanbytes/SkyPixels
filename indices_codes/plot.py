import numpy
from rasterio import plot
import math
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show


'''
# Open the TIFF file
with rasterio.open('ndvi.tif') as src:
    # Read the file into a NumPy array
    ndvi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
ndvi_min = np.min(ndvi_data)
ndvi_max = np.max(ndvi_data)

ndvi = rasterio.open('ndvi.tif')
plot.show(ndvi, title='NDVI')

print(ndvi_min)
print(ndvi_max)



# Open the TIFF file
with rasterio.open('gndvi.tif') as src:
    # Read the file into a NumPy array
    gndvi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
gndvi_min = np.min(gndvi_data)
gndvi_max = np.max(gndvi_data)

gndvi = rasterio.open('gndvi.tif')
plot.show(gndvi, title='GNDVI')

print(gndvi_min)
print(gndvi_max)


		
# Open the TIFF file
with rasterio.open('ndre.tif') as src:
    # Read the file into a NumPy array
    ndre_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
ndre_min = np.min(ndre_data)
ndre_max = np.max(ndre_data)

ndre = rasterio.open('ndre.tif')
plot.show(ndre, title='NDRE')

print(ndre_min)
print(ndre_max)



# Open the TIFF file
with rasterio.open('mcari.tif') as src:
    # Read the file into a NumPy array
    mcari_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
mcari_min = np.min(mcari_data)
mcari_max = np.max(mcari_data)

mcari = rasterio.open('mcari.tif')
plot.show(mcari, title='MCARI')

print(mcari_min)
print(mcari_max)



# Open the TIFF file
with rasterio.open('osavi.tif') as src:
    # Read the file into a NumPy array
    osavi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
osavi_min = np.min(osavi_data)
osavi_max = np.max(osavi_data)

osavi = rasterio.open('osavi.tif')
plot.show(osavi, title='OSAVI')

print(osavi_min)
print(osavi_max)



# Open the TIFF file
with rasterio.open('endvi.tif') as src:
    # Read the file into a NumPy array
    endvi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
endvi_min = np.min(endvi_data)
endvi_max = np.max(endvi_data)

endvi = rasterio.open('endvi.tif')
plot.show(endvi, title='ENDVI')

print(endvi_min)
print(endvi_max)



# Open the TIFF file
with rasterio.open('gbvi.tif') as src:
    # Read the file into a NumPy array
    gbvi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
gbvi_min = np.min(gbvi_data)
gbvi_max = np.max(gbvi_data)

gbvi = rasterio.open('gbvi.tif')
plot.show(gbvi, title='GBVI')

print(gbvi_min)
print(gbvi_max)


'''
'''
# Open the TIFF file
with rasterio.open('/nmhs2/hari/work/UAV/indices/ktym/feb2024/field1/0004SET/evi.tif') as src:
    # Read the file into a NumPy array
    evi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
evi_min = np.min(evi_data)
evi_max = np.max(evi_data)

evi = rasterio.open('/nmhs2/hari/work/UAV/indices/ktym/feb2024/field1/0004SET/evi.tif')
plot.show(evi, title='EVI')

print(evi_min)
print(evi_max)
'''

'''
# Open the TIFF file
with rasterio.open('evi.tif') as src:
    # Read the file into a NumPy array
    evi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
evi_min = np.min(evi_data)
evi_max = np.max(evi_data)

evi = rasterio.open('evi.tif')
plot.show(evi, title='EVI')

print(evi_min)
print(evi_max)

'''


# Open the TIFF file
with rasterio.open('/nmhs2/hari/work/UAV/indices/ktym/jan2024/field1/0011SET/evi.tif') as src:
    # Read the file into a NumPy array
    evi_data = src.read(1)  # assuming the data is in the first band
    
    # Calculate the minimum and maximum values
    evi_min = np.min(evi_data)
    evi_max = np.max(evi_data)

    # Plot the data with a colorbar
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    cax = ax.imshow(evi_data, cmap='viridis', vmin=evi_min, vmax=evi_max)
    ax.set_title('EVI ')
    cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
    cbar.set_label('EVI Value')
    plt.savefig('evi.png')
    plt.show()

print(f"EVI Min: {evi_min}")
print(f"EVI Max: {evi_max}")

'''
# Open the TIFF file
with rasterio.open('lai2.tif') as src:
    # Read the file into a NumPy array
    lai_data = src.read(1)  # assuming the data is in the first band
    
    # Calculate the minimum and maximum values
    lai_min = np.min(lai_data)
    lai_max = np.max(lai_data)

    # Plot the data with a colorbar
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    cax = ax.imshow(lai_data, cmap='viridis', vmin=lai_min, vmax=lai_max)
    ax.set_title('LAI 2')
    cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
    cbar.set_label('LAI Value')
    plt.show()

print(f"LAI Min: {lai_min}")
print(f"LAI Max: {lai_max}")
'''
