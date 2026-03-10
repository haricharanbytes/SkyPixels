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


np.seterr(divide='ignore', invalid='ignore')  # Allow division by zero
savi = np.empty(red.shape, dtype=rasterio.float32)  # Create empty matrix


# calculate savi

savi = np.where((nir+red+0.5)==0., 0,  (nir - red)* (1+0.5) /(nir + red + 0.5))  

saviImage = rasterio.open('savi.tif','w',driver = 'GTiff',width=redband.width, height=redband.height, count=1 ,crs=redband.crs ,transform=redband.transform ,dtype='float32')
saviImage.write(savi,1)
saviImage.close()

# Open the TIFF file
with rasterio.open('savi.tif') as src:
    # Read the file into a NumPy array
    savi_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
savi_min = np.min(savi_data)
savi_max = np.max(savi_data)

savi = rasterio.open('savi.tif')
plot.show(savi, title='savi')

print(savi_min)
print(savi_max)
