import numpy
from rasterio import plot
import math
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show

with rasterio.open('path') as src:
    # Read the file into a NumPy array
    evi_data = src.read(1)  # assuming the data is in the first band
    
    # Calculate the minimum and maximum values
    evi_min = np.min(evi_data)
    evi_max = np.max(evi_data)

    # Plot the data with a colorbar
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    cax = ax.imshow(evi_data, cmap='Blues', vmin=evi_min, vmax=evi_max)
    ax.set_title('tif')
    cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
    cbar.set_label('tif Value')
    #plt.savefig('gcvi.png')
    plt.show()

print('max:', evi_max)
print('min:', evi_min)
