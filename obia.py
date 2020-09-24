"""
Created on Tue Sep 22 00:08:42 2020

@author: Alaisha Naidu
Name: Object Based Image Analysis (OBIA)
Creds: USGS and Open Source Options
"""


import numpy as np
import scipy
import gdal #to read raster data

sentinel2_fn = "#enter pathname"

driverTiff = gdal.GetDriverByName("GTiff")
sentinel2_ds = gdal.Open(sentinel2_fn)

nbands = sentinel2_ds.RasterCount #number of bands of imagery

band_data = [] #empty list

print('bands', sentinel2_ds.RaterCount, 'rows', sentinel2_ds.RaterYSize(), 'coloumns', sentinel2_ds.RaterXSize())

for i in range(1, nbands+1): #loop through bands and save data from 1 band to nbands +1
    band = sentinel2_ds.GetRasterBand(i).ReadAsArray() #reads data as a numpy array
    band_data.append(band)
band_data = np.dstack(b for b in band_data) #loop through all the bands and stack them together
