import numpy
from rasterio import plot
import math
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import rasterio
from rasterio.plot import show



blueband  = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/bands/orthomosaic_band1.tif')
greenband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/bands/orthomosaic_band2.tif')
redband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/bands/orthomosaic_band3.tif')
rededgeband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/bands/orthomosaic_band4.tif')
nirband = rasterio.open('/nmhs2/csirmission/HCP_57/uav_processed_agisoft/nagercoil/sept2024_second_season/regular_mission/0005SET/bands/orthomosaic_band5.tif')


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
osavi = np.empty(nir.shape, dtype=rasterio.float32)

# Calculate OSAVI
osavi = np.where((nir+red)==0., 0,  (nir - red)/(nir + red+0.16)) 

# Save OSAVI to a new file
osaviImage = rasterio.open(
    'osavi.tif', 'w',
    driver='GTiff',
    width=nirband.width,
    height=nirband.height,
    count=1,
    crs=nirband.crs,
    transform=nirband.transform,
    dtype='float32'
)

osaviImage.write(osavi, 1)
osaviImage.close()

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
