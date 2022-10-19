"""
Checking realism (or lack thereof) in HadGEM biogeochemical output
"""

#Import libraries
import numpy as np
import xarray as xr
import scipy
from scipy import stats
import scipy.special as sp
import cftime
import matplotlib.pyplot as plt
from matplotlib import cm
import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.util import add_cyclic_point
from glob import glob
import os
import warnings

#Set paths
data_dir = '/Users/mdiamond/Data/CMIP5/HadGEM2-ES'

"""
Load data
"""

fxa = xr.open_mfdataset(glob(data_dir+'/*a_fx*nc')+glob(data_dir+'/*orog_fx*nc')+glob(data_dir+'/*sftlf_fx*nc'))
fxo = xr.open_mfdataset(glob(data_dir+'/*o_fx*nc')+glob(data_dir+'/*sftof_fx*nc'))
fxo['basin'] = xr.open_dataset(glob(data_dir+'/*basin_fx*nc')[0])['basin'] #Error when trying to load at same time as other ocean fx variables

da = {} #Atmospheric data
do = {} #Ocean data

vars_atm = ['od550aer', 'reffclwtop', 'clt', 'evspsbl', 'pr', 'rlut', 'rsds', 'rsdscs', 'rsdt', 'rsut', 'rsutcs', 'tas']
vars_ocn = ['chl', 'chldiat', 'chlmisc', 'dms', 'intpdiat', 'intpmisc', 'intpp', 'o2', 'o2min', 'ph', 'phyc', 'phydiat', 'phymisc', 'so', 'sos', 'talk', 'tos', 'zooc', 'zsatarag', 'zsatcalc']

print('Loading data...')
for exp in ['rcp45','G4','G4cdnc']: #Separate ocean and atmospheric datasets
    print(exp)
    
    files_atm = []
    files_ocn = []
    
    for vara in vars_atm: files_atm = files_atm + glob(data_dir+'/*%s_*%s_*r1i1p1*nc' % (vara,exp))
    for varo in vars_ocn: files_ocn = files_ocn + glob(data_dir+'/*%s_*%s_*r1i1p1*nc' % (varo,exp))
        
    da[exp] = xr.open_mfdataset(files_atm)
    do[exp] = xr.open_mfdataset(files_ocn)
    
    #Unit conversions and variable transformations
    
print('...Done!')

















