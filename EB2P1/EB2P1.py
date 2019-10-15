#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:29:28 2019

@author: macbookair
"""

import numpy as np
from matplotlib import pyplot as plt
import cartopy.feature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
import os
import xarray as xr


ruta="/Users/macbookair/Desktop/practicasCG/atmo/Practica 2/EB2P1/" #ruta CARO
os.chdir(ruta)
dir = 'EB2P1.nc'
dS = xr.open_dataset(dir, decode_times=False)
print(dS)       # visualizo la info del .nc
phi=dS['stream'].values
time=dS['time'].values
lon=dS['lon'].values
lat=dS['lat'].values
lons, lats = np.meshgrid(lon, lat)

#%%ANOMALIAS EB1P2

a = np.mean(phi[49,:,:], axis=1)
b = np.mean(np.mean(phi[50:59,:,:], axis=0), axis=1)
lons, a = np.meshgrid(lon,a)
lons, b = np.meshgrid(lon,b)
phiz = phi[49,:,:] - a + b

phia = np.empty((10,128,256))
for i in range (10):
    phia[i,:,:] = phi[i+50,:,:] - phiz

#TODO EL DOMINIO
#dia 2
plt.imshow(phia[1,:,:]) 
plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax = 6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 0
LONMAX= 359.9
LATMIN = -90
LATMAX = 90
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[1,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label='10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(0, 360, 60), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 90, 30), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 2", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 2.jpg')

#dia 4

plt.imshow(phia[3,:,:]), plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax = 6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 0
LONMAX= 359.9
LATMIN = -90
LATMAX = 90
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[3,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label='10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(0, 360, 60), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 90, 30), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 4", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 4.jpg')

#dia 8

plt.imshow(phia[7,:,:]), plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax = 6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 0
LONMAX= 359.9
LATMIN = -90
LATMAX = 90
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[7,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label='10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(0, 360, 60), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 90, 30), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 8", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 8.jpg')

#%%
#(90àS–10àN) X (60àE–180àO)

#dia 2
plt.imshow(phia[1,:,:]), plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax = 6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 60
LONMAX= 240
LATMIN = -90
LATMAX = 10
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[3,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label=' 10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(60, 240, 30), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 10, 20), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 2", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 2b.jpg')

#dia 4

plt.imshow(phia[3,:,:]), plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax = 6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 60
LONMAX= 240
LATMIN = -90
LATMAX = 10
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[3,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label=' 10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(60, 240, 30), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 10, 20), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 4", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 4b.jpg')

#dia 8

plt.imshow(phia[7,:,:]), plt.colorbar() #hago un grafico pra visualizar min y max
cmin = -6
cmax =  6
ncont = 13
clevs = np.linspace(cmin, cmax, ncont)
fig=plt.figure(figsize=(6,4),dpi=200)
LONMIN= 60
LONMAX= 240
LATMIN = -90
LATMAX = 10
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
crs_latlon = ccrs.PlateCarree()
ax.set_extent([LONMIN, LONMAX, LATMIN, LATMAX], crs=crs_latlon)
im=ax.contourf(lons, lats, phia[7,:,:]/1e6, clevs, cmap=plt.get_cmap("RdBu"), extend='both', transform=crs_latlon)
plt.colorbar(im, fraction=0.052, pad=0.08, shrink=0.8, aspect=20, orientation='horizontal', label='10$^{6}$ x m$^{2}$ s$^{-1}$')
ax.add_feature(cartopy.feature.LAND, facecolor='#d9d9d9')
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.gridlines(crs=crs_latlon, linewidth=0.3, linestyle='-')
ax.set_xticks(np.arange(60, 240, 60), crs=crs_latlon)
ax.set_yticks(np.arange(-90, 10, 30), crs=crs_latlon)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.title("Anomalia EB2P1 dia 8", fontsize=8, y=0.98, loc="center")
plt.savefig('Anomalia EB2P1 dia 8b.jpg')

#%%diagrama de Hovmoller

# latitud -28 posicion 43
# lon 220 posicion 157

maxes=np.max(phia[:,43,:])
mins=np.min(phia[:,43,:])
print ('maxes are :' ,maxes ,'\nmins are : ', mins)
np.where(phia[:,43,:] == np.amax(np.array(phia[:,43,:]))) # 3 43 177
np.where(phia[:,43,:] == np.amin(np.array(phia[:,43,:]))) #1 43 152
levels_psi=np.arange(-60,90,15)

plt.figure()
plt.contourf(phia[:,43,:]/1e5,levels=levels_psi,cmap='RdYlGn')
plt.plot(np.linspace(6081184.0 /1e5,-5756862.0/1e5))
plt.ylabel("Tiempo")
plt.xlabel("Longitud")
cbar=plt.colorbar()
cbar.ax.set_title("x10$^{5}$ m${2}$ s$^{-1}$")
plt.title('Hovmoller Meridional EB2P1')
plt.savefig('Hovmoller Meridional EB2P1.png')


plt.figure()
plt.contourf(phia[:,:,157]/1e5,levels=levels_psi, cmap='RdYlGn')
plt.ylabel("Tiempo")
plt.xlabel("Latitud")
cbar=plt.colorbar()
cbar.ax.set_title("x10$^{5}$ m${2}$ s$^{-1}$")
plt.title('Hovmoller Zonal EB2P1')
plt.savefig('Hovmoller Zonal EB2P1.png')


