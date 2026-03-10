import numpy
from rasterio import plot
import math
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show

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

