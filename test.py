# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:25:06 2020

@author: ryan-
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate

#%%
# For loop file pathing
folder_path = "./csv_backup/"
#Length of orbit in minutes approx
orbit_length = 93 
# this is used in for loops to get data from sheets
chunksize = orbit_length

dim = (orbit_length, 1)

#temporarily holds csv data in for loops
# 3U data
port_list = np.zeros(dim)
port_dep_list = np.zeros(dim)
star_list = np.zeros(dim)
star_dep_list = np.zeros(dim)
zenith_list = np.zeros(dim)

# 2U data
hd_pd_list = np.zeros(dim)
hd_p_list = np.zeros(dim)
hd_sd_list = np.zeros(dim)
hd_s_list = np.zeros(dim)
hd_z_list = np.zeros(dim)
ND_p_list = np.zeros(dim)
ND_s_list = np.zeros(dim)
ND_z_list = np.zeros(dim)

#stores power data from csv files
port_orbit_power = []
port_dep_orbit_power = []
star_orbit_power = []
star_dep_orbit_power = []
zenith_orbit_power = []

hd_pd_power = []
hd_p_power = []
hd_sd_power = []
hd_s_power = []
hd_z_power = []

ND_p_power = []
ND_s_power = []
ND_z_power = []


# will store energy calculations from csv
port_energy = []
port_dep_energy = []
star_energy = []
star_dep_energy = []
zenith_energy = []

hd_pd_energy = []
hd_p_energy = []
hd_sd_energy = []
hd_s_energy = []
hd_z_energy = []

ND_p_energy = []
ND_s_energy = []
ND_z_energy = []

total_energy = []
#%%
# =============================================================================
# This chuncks up the data into parts of 93 (each for one orbit), it takes the power portion
# and integrates it over the 93 minutes
# It then concatenates it onto the energy list
# Also puts raw power data in a list
# =============================================================================
for chunk in pd.read_csv(folder_path +"EX2-Port-Power.csv", chunksize=chunksize):
    port_list=(chunk.iloc[:,1])
    try:
        port_energy.append(integrate.cumtrapz(port_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        port_orbit_power.append(port_list)
    except:
        pass


for chunk in pd.read_csv(folder_path +"EX2-PortDep-Power.csv", chunksize=chunksize):
    port_dep_list=(chunk.iloc[:,1])
    try:
        port_dep_energy.append(integrate.cumtrapz(port_dep_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        port_dep_orbit_power.append(port_dep_list)
    except:
        pass


for chunk in pd.read_csv(folder_path +"EX2-Star-Power.csv", chunksize=chunksize):
    star_list=(chunk.iloc[:,1])
    try:
        star_energy.append(integrate.cumtrapz(star_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        star_orbit_power.append(star_list)
    except:
        pass
        
for chunk in pd.read_csv(folder_path +"EX2-StarDep-Power.csv", chunksize=chunksize):
    star_dep_list=(chunk.iloc[:,1])
    try:
        star_dep_energy.append(integrate.cumtrapz(star_dep_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        star_dep_orbit_power.append(star_dep_list)
    except:
        pass


for chunk in pd.read_csv(folder_path +"EX2-Zenith-Power.csv", chunksize=chunksize):
    zenith_list=(chunk.iloc[:,1])
    try:
        zenith_energy.append(integrate.cumtrapz(zenith_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        zenith_orbit_power.append(zenith_list)
    except:
        pass

for chunk in pd.read_csv(folder_path +"2U_HalfDep-PortDep-Power.csv", chunksize=chunksize):
    hd_pd_list=(chunk.iloc[:,1])
    try:
        hd_pd_energy.append(integrate.cumtrapz(hd_pd_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        hd_pd_power.append(hd_pd_list)
    except:
        pass    

for chunk in pd.read_csv(folder_path +"2U_HalfDep-Port-Power.csv", chunksize=chunksize):
    hd_p_list=(chunk.iloc[:,1])
    try:
        hd_p_energy.append(integrate.cumtrapz(hd_p_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        hd_p_power.append(hd_p_list)
    except:
        pass  

for chunk in pd.read_csv(folder_path +"2U_HalfDep-StarDep-Power.csv", chunksize=chunksize):
    hd_sd_list=(chunk.iloc[:,1])
    try:
        hd_sd_energy.append(integrate.cumtrapz(hd_sd_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        hd_sd_power.append(hd_sd_list)
    except:
        pass  

for chunk in pd.read_csv(folder_path +"2U_HalfDep-Star-Power.csv", chunksize=chunksize):
    hd_s_list=(chunk.iloc[:,1])
    try:
        hd_s_energy.append(integrate.cumtrapz(hd_s_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        hd_s_power.append(hd_s_list)
    except:
        pass  

for chunk in pd.read_csv(folder_path +"2U_HalfDep-Zenith-Power.csv", chunksize=chunksize):
    hd_z_list=(chunk.iloc[:,1])
    try:
        hd_z_energy.append(integrate.cumtrapz(hd_z_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        hd_z_power.append(hd_z_list)
    except:
        pass  

for chunk in pd.read_csv(folder_path +"2U_NoDep-Port-Power.csv", chunksize=chunksize):
    ND_p_list=(chunk.iloc[:,1])
    try:
        ND_p_energy.append(integrate.cumtrapz(ND_p_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        ND_p_power.append(ND_p_list)
    except:
        pass  

for chunk in pd.read_csv(folder_path +"2U_NoDep-Star-Power.csv", chunksize=chunksize):
    ND_s_list=(chunk.iloc[:,1])
    try:
        ND_s_energy.append(integrate.cumtrapz(ND_s_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        ND_s_power.append(ND_s_list)
    except:
        pass 

for chunk in pd.read_csv(folder_path +"2U_NoDep-Zenith-Power.csv", chunksize=chunksize):
    ND_z_list=(chunk.iloc[:,1])
    try:
        ND_z_energy.append(integrate.cumtrapz(ND_z_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
        ND_z_power.append(ND_z_list)
    except:
        pass  


#%%    
# =============================================================================
# Calculates the total energy and puts it into a numpy array as other modules can use that
# and values can be added together
# =============================================================================

# 3U no failure
portnrg_array = np.array(port_energy)
portdepnrg_array = np.array(port_dep_energy)
starnrg_array = np.array(star_energy)
stardepnrg_array = np.array(star_dep_energy)
zenithnrg_array = np.array(zenith_energy)

# 3U one dep
# portnrg_array = 0
# portdepnrg_array = np.array(port_energy)
# starnrg_array = np.array(star_energy)
# stardepnrg_array = np.array(star_dep_energy)
# zenithnrg_array = np.array(zenith_energy)

# 3U full failure
# portnrg_array = 0
# portdepnrg_array = np.array(port_energy)
# starnrg_array = 0
# stardepnrg_array = np.array(star_energy)
# zenithnrg_array = np.array(zenith_energy)

# 2U no failure, with no deployables
# portnrg_array = np.array(ND_p_energy)
# portdepnrg_array = 0
# starnrg_array = np.array(ND_s_energy)*2
# stardepnrg_array = 0
# zenithnrg_array = np.array(ND_z_energy) *1/2

# 2U no failure, with half deployables
# portnrg_array = np.array(hd_p_energy)
# portdepnrg_array = np.array(hd_pd_energy)
# starnrg_array = np.array(hd_s_energy)*2
# stardepnrg_array = np.array(hd_sd_energy)
# zenithnrg_array = np.array(hd_z_energy) /2

# 2U no failure, with full deployables
# portnrg_array = np.array(hd_p_energy)
# portdepnrg_array = np.array(hd_pd_energy)*2
# starnrg_array = np.array(hd_s_energy)*2
# stardepnrg_array = np.array(hd_sd_energy)*2
# zenithnrg_array = np.array(hd_z_energy) *1/2

# 2U half failure, with half deployables
# portnrg_array = np.array(hd_p_energy)/3
# portdepnrg_array = np.array(hd_p_energy)/2
# starnrg_array = np.array(hd_s_energy)*2
# stardepnrg_array = np.array(hd_sd_energy)
# zenithnrg_array = np.array(hd_z_energy) *1/2

# 2U full failure, with half deployables
# portnrg_array = np.array(hd_p_energy)/3
# portdepnrg_array = np.array(hd_p_energy)/2
# starnrg_array = np.array(hd_s_energy)*2/3
# stardepnrg_array = np.array(hd_s_energy)
# zenithnrg_array = np.array(hd_z_energy) *1/2

# 2U half failure, with full deployables
# portnrg_array = 0
# portdepnrg_array = np.array(hd_p_energy)
# starnrg_array = np.array(hd_s_energy)*2
# stardepnrg_array = np.array(hd_sd_energy)
# zenithnrg_array = np.array(hd_z_energy) *1/2

# 2U full failure, with full deployables
# portnrg_array = 0
# portdepnrg_array = np.array(hd_p_energy)
# starnrg_array = 0
# stardepnrg_array = np.array(hd_s_energy)*2
# zenithnrg_array = np.array(hd_z_energy) *1/2

# calculating total energy and turning it into from Wmin to Whr
total_energy= portnrg_array/60+portdepnrg_array/60+starnrg_array/60+stardepnrg_array/60+zenithnrg_array/60
# Turning Wmin into Watt
total_power= portnrg_array/orbit_length+portdepnrg_array/orbit_length+starnrg_array/orbit_length+stardepnrg_array/orbit_length+zenithnrg_array/orbit_length

print(total_energy)
print(total_power)


# # Finding data values for min, max, mean for selected range
# dataend = int(np.floor(len(total_power)/2))

# # Finding data values for min, max, mean energy
# emin = total_energy[0:dataend].min()
# emean = total_energy[0:dataend].mean()
# emax = total_energy[0:dataend].max()

# # Finding data values for min, max, mean power
# pmin = total_power[0:dataend].min()
# pmean = total_power[0:dataend].mean()
# pmax = total_power[0:dataend].max()

# # finding index for them in the data, mean doesn't have an index
# emin_idx = np.where(total_energy == emin)[0]
# # most specific number where the mean rounds to an actual value (thousandth), 2 of them so i just chose first one
# emean_idx = np.where(np.round(total_energy,3) == round(emean,3))[0][0]
# emax_idx = np.where(total_energy == emax)[0]

# pmean_idx = np.where(np.round(total_power,3) == round(pmean,3))[0]
# pmin_idx = np.where(total_power == pmin)[0]
# pmean_idx = np.where(np.round(total_power,3) == round(pmean,3))[0][0]
# pmax_idx = np.where(total_power == pmax)[0]



# #emean_orbit = (port_list[:,99].mean()+port_dep_list[:,99].mean()+star_list[:,99].mean()+star_dep_list[:,99].mean()+zenith_list[:,99].mean())
# print("Min, idx: " + str(emin) + ", " + str(emin_idx))
# print("Mean, idx: " + str(emean) + ", " + str(emean_idx))
# print("Max, idx: " + str(emax) + ", " + str(emax_idx))
# #print("Mean Power: " + str(emean_orbit))

# print("Min, idx: " + str(pmin) + ", " + str(pmin_idx))
# print("Mean, idx: " + str(pmean) + ", " + str(pmean_idx))
# print("Max, idx: " + str(pmax) + ", " + str(pmax_idx))