import numpy
from rasterio import plot
import math
import matplotlib.pyplot as plt
from scipy import stats
from pandas.api.types import CategoricalDtype
import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show



blueband  = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/ngl_large_field_mission_2/0004SET/bands/orthomosaic_band1.tif')
greenband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/ngl_large_field_mission_2/0004SET/bands/orthomosaic_band2.tif')
redband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/ngl_large_field_mission_2/0004SET/bands/orthomosaic_band3.tif')
rededgeband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/ngl_large_field_mission_2/0004SET/bands/orthomosaic_band4.tif')
nirband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/ngl_large_field_mission_2/0004SET/bands/orthomosaic_band5.tif')


blue = np.array(blueband)
green = np.array(greenband)
red = np.array(redband)
rededge = np.array(rededgeband)
nir = np.array(nirband)


red = redband.read(1).astype(float)
nir = nirband.read(1).astype(float)
green = greenband.read(1).astype(float)
blue =  blueband.read(1).astype(float)
rededge = rededgeband.read(1).astype(float)

redband.height
redband.width
redband.dtypes[0]
redband.crs
redband.transform
redband.read(1)


greenband.height
greenband.width
greenband.dtypes[0]
greenband.crs
greenband.transform
greenband.read(1)


blueband.height
blueband.width
blueband.dtypes[0]
blueband.crs
blueband.transform
blueband.read(1)


# Allow division by zero
np.seterr(divide='ignore', invalid='ignore')

# Create empty matrix
endvi = np.empty(nir.shape, dtype=rasterio.float32)

# Calculate endvi
endvi =np.where((nir + green + 2 * blue) == 0., 0, (nir + green - 2 * blue) / (nir + green + 2 * blue))

# Save GNDVI to a new file
endviImage = rasterio.open(
    'endvi.tif', 'w',
    driver='GTiff',
    width=greenband.width,
    height=greenband.height,
    count=1,
    crs=greenband.crs,
    transform=greenband.transform,
    dtype='float32'
)

endviImage.write(endvi, 1)
endviImage.close()

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
