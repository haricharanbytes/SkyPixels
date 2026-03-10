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
vari = np.empty(red.shape, dtype=rasterio.float32)  # Create empty matrix


# calculate vari

vari = np.where((green + red - blue)==0., 0,  (green - red)/(green + red - blue))  

variImage = rasterio.open('vari.tif','w',driver = 'GTiff',width=redband.width, height=redband.height, count=1 ,crs=redband.crs ,transform=redband.transform ,dtype='float32')
variImage.write(vari,1)
variImage.close()

# Open the TIFF file
with rasterio.open('vari.tif') as src:
    # Read the file into a NumPy array
    vari_data = src.read(1)  # assuming the data is in the first band

# Calculate the minimum and maximum values
vari_min = np.min(vari_data)
vari_max = np.max(vari_data)

vari = rasterio.open('vari.tif')
plot.show(vari, title='vari')

print(vari_min)
print(vari_max)
