import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup as bs

from mpl_toolkits.basemap import Basemap, shiftgrid
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.location import Location

import xarray as xr
import cftime
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import hvplot.xarray

import matplotlib.pyplot as plt
from matplotlib import colors as c
#-------------------------------------------- Maquillamos el dataaset que me he descargado de la esa


'''map_df=xr.open_dataset('../data/sea_level_phase.nc')

ds = map_df.rename(time='time_step')
print(ds.time_step)

# Time encoding properties
dtype = ds.time_step.encoding['dtype']
units = ds.time_step.encoding['units']

# Get the time boundary values
ts       = ds.time_step.values
ts_start = ts[0]
ts_end   = ts[-1]
ts_mid   = ts_start + 0.5 * (ts_end - ts_start)

# New coordinate variables according to CF
time      = xr.DataArray(np.array([ts_mid]), dims='time')
time_bnds = xr.DataArray(np.array([[ts_start, ts_end]]), dims=['time', 'bnds'])

# Assign coordinate variables
ds = ds.assign_coords(time=time, time_bnds=time_bnds)

# Update coordinate variable attributes according to CF
ds.time.attrs.update(bounds='time_bnds')

# Set coordinate variable encodings
ds.time.encoding.update(units=units, dtype=dtype)
ds.time_bnds.encoding.update(units=units, dtype=dtype)

ds['ampl'] = ds.ampl.expand_dims('time')
ds['phase'] = ds.phase.expand_dims('time')

ds = ds.transpose('time', 'bnds', 'time_step', 'period', 'lat', 'lon')

ds.to_netcdf('../data/sea_level_phase(act).nc')'''

#-------------------------------------------- Ahora sí, las funciones que vamos a utilizar



