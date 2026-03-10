import numpy as np
import rasterio
from rasterio.plot import show

# Open the NDVI image
with rasterio.open('ndvi.tif') as ndvi_dataset:
    ndvi = ndvi_dataset.read(1).astype(float)

    # Allow division by zero
    np.seterr(divide='ignore', invalid='ignore')

    # Create the LAI matrix
    lai = 0.1524 * np.exp(3.4927 * ndvi)

    # Prepare metadata for the output file
    lai_meta = ndvi_dataset.meta.copy()
    lai_meta.update({
        'dtype': 'float32',
        'count': 1
    })

    # Write the LAI image
    with rasterio.open('lai.tif', 'w', **lai_meta) as lai_image:
        lai_image.write(lai.astype('float32'), 1)

lai_min = np.min(lai)
lai_max = np.max(lai)

ndvi = rasterio.open('lai.tif')
show(ndvi, title='LAI')

print('lai minimum :', lai_min)
print('lai maximum :', lai_max)

