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


# Finding data values for min, max, mean for selected range
dataend = int(np.floor(len(total_power)/2))

# Finding data values for min, max, mean energy
emin = total_energy[0:dataend].min()
emean = total_energy[0:dataend].mean()
emax = total_energy[0:dataend].max()

# Finding data values for min, max, mean power
pmin = total_power[0:dataend].min()
pmean = total_power[0:dataend].mean()
pmax = total_power[0:dataend].max()

# finding index for them in the data, mean doesn't have an index
emin_idx = np.where(total_energy == emin)[0]
# most specific number where the mean rounds to an actual value (thousandth), 2 of them so i just chose first one
emean_idx = np.where(np.round(total_energy,3) == round(emean,3))[0][0]
emax_idx = np.where(total_energy == emax)[0]

pmean_idx = np.where(np.round(total_power,3) == round(pmean,3))[0]
pmin_idx = np.where(total_power == pmin)[0]
pmean_idx = np.where(np.round(total_power,3) == round(pmean,3))[0][0]
pmax_idx = np.where(total_power == pmax)[0]



# emean_orbit = (port_list[:,99].mean()+port_dep_list[:,99].mean()+star_list[:,99].mean()+star_dep_list[:,99].mean()+zenith_list[:,99].mean())
# print("Min, idx: " + str(emin) + ", " + str(emin_idx))
# print("Mean, idx: " + str(emean) + ", " + str(emean_idx))
# print("Max, idx: " + str(emax) + ", " + str(emax_idx))
# print("Mean Power: " + str(emean_orbit))

# print("Min, idx: " + str(pmin) + ", " + str(pmin_idx))
# print("Mean, idx: " + str(pmean) + ", " + str(pmean_idx))
# print("Max, idx: " + str(pmax) + ", " + str(pmax_idx))

#%%
# =============================================================================
# Displaying Power Generated Per Orbit of ExAlta 2
# =============================================================================

# declaring variable sizes for plotting
orbit_total = len(total_power)
orbit_count_to_day = orbit_length/60/24
days_total = orbit_total * orbit_count_to_day
straight_line = np.ones(orbit_total)

font = {'family' : 'serif',
        'sans-serif' : 'helvetica',
        'size'   : 20}

plt.rc('font', **font)

fig = plt.figure(figsize=(16, 8), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

            
ax1 = plt.subplot(1,1,1)
ax1.plot(np.linspace(0,days_total,orbit_total),zenithnrg_array/orbit_length,linewidth = 2, color ='dodgerblue',label='Zenith')
ax1.plot(np.linspace(0,days_total,orbit_total),portdepnrg_array/orbit_length,linewidth = 2,color ='blue',label='Port Deployable')
ax1.plot(np.linspace(0,days_total,orbit_total),portnrg_array/orbit_length,linewidth = 2,color ='red',label='Port')
ax1.plot(np.linspace(0,days_total,orbit_total),starnrg_array/orbit_length,linewidth = 2,color ='darkred',label='Starboard')
ax1.plot(np.linspace(0,days_total,orbit_total),stardepnrg_array/orbit_length,linewidth = 2,color ='darkviolet',label='Starboard Deployable')
ax1.plot(np.linspace(0,days_total,orbit_total),pmax*straight_line,'darkgreen', linestyle ='--',linewidth = 2,label='Max')
ax1.plot(np.linspace(0,days_total,orbit_total),pmin*straight_line,'chartreuse', linestyle ='--',linewidth = 2,label='Min')
ax1.plot(np.linspace(0,days_total,orbit_total),pmean*straight_line,'limegreen', linestyle ='--',linewidth = 2,label='Mean')
ax1.plot(np.linspace(0,days_total,orbit_total),total_power,linewidth = 2,color = 'k',label='Total')
ax1.plot(np.linspace(0,days_total,orbit_total),pmax*straight_line,'darkgreen', linestyle ='--',linewidth = 2,label='Max')

#for when port and starboard are 0
# ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='red',label='Port')
# ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='darkred',label='Starboard')

ax1.legend(loc=0, fontsize = 20, ncol = 3)
ax1.set_xlim([0,364])
ax1.set_ylim([-.5, 9])

ax1.set_xlabel('Time (Day)', fontsize = 25)
ax1.set_ylabel('Power (W)', fontsize = 25)
ax1.set_title('Power generated per orbit of ExAlta 2', fontsize = 30, pad=20)
plt.savefig("test3.png")
#%%

# =============================================================================
# Displaying Power generated over worst and best case orbits (turn on power variables to use this)
# =============================================================================

# font information

font = {'family' : 'serif',
        'sans-serif' : 'helvetica',
        'size'   : 20}

plt.rc('font', **font)

# figure information
fig = plt.figure(figsize=(12, 10), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

# subplots,row,column
ax1 = plt.subplot(3,1,1)
# ax1.xaxis.tick_top()
ax1.plot(np.linspace(0,orbit_length,orbit_length),port_orbit_power[int(emin_idx)],linewidth = 3,label='Port')
ax1.plot(np.linspace(0,orbit_length,orbit_length),port_dep_orbit_power[int(emin_idx)],linewidth = 3,label='Port Deployable')
ax1.plot(np.linspace(0,orbit_length,orbit_length),star_orbit_power[int(emin_idx)],linewidth = 3,label='Starboard')
ax1.plot(np.linspace(0,orbit_length,orbit_length),star_dep_orbit_power[int(emin_idx)],linewidth = 3,label='Starboard Deployable')
ax1.plot(np.linspace(0,orbit_length,orbit_length),zenith_orbit_power[int(emin_idx)],linewidth = 3,label='Zenith')
ax1.legend(loc=1, fontsize = 17, ncol = 3)
ax1.set_ylim([-0.5, 9.5])

ax2 = plt.subplot(3,1,2)
ax2.plot(np.linspace(0,orbit_length,orbit_length),port_orbit_power[int(emax_idx)],linewidth = 3,label='Port')
ax2.plot(np.linspace(0,orbit_length,orbit_length),port_dep_orbit_power[int(emax_idx)],linewidth = 3,label='Port Deployable')
ax2.plot(np.linspace(0,orbit_length,orbit_length),star_orbit_power[int(emax_idx)],linewidth = 3,label='Starboard')
ax2.plot(np.linspace(0,orbit_length,orbit_length),star_dep_orbit_power[int(emax_idx)],linewidth = 3,label='Starboard Deployable')
ax2.plot(np.linspace(0,orbit_length,orbit_length),zenith_orbit_power[int(emax_idx)],linewidth = 3,label='Zenith')
# ax2.legend(loc=0, fontsize = 20, ncol = 3)
ax2.set_ylim([-0.5,9.5])

ax3 = plt.subplot(3,1,3)
ax3.plot(np.linspace(0,orbit_length,orbit_length), port_orbit_power[emean_idx],linewidth = 3,label='Port')
ax3.plot(np.linspace(0,orbit_length,orbit_length), port_dep_orbit_power[emean_idx],linewidth = 3,label='Port Deployable')
ax3.plot(np.linspace(0,orbit_length,orbit_length),star_orbit_power[emean_idx],linewidth = 3,label='Starboard')
ax3.plot(np.linspace(0,orbit_length,orbit_length),star_dep_orbit_power[emean_idx],linewidth = 3,label='Starboard Deployable')
ax3.plot(np.linspace(0,orbit_length,orbit_length),zenith_orbit_power[emean_idx],linewidth = 3,label='Zenith')
#ax2.legend(loc=0, fontsize = 20, ncol = 3)
ax2.set_ylim([-0.5,9.5])

ax3.set_xlabel('Time (Minute)', fontsize = 25)
ax1.set_ylabel(r"Power$_\mathrm{min}$ (W)", fontsize = 20)
ax2.set_ylabel(r"Power$_\mathrm{max}$ (W)", fontsize = 20)
ax3.set_ylabel(r"Power$_\mathrm{mean}$ (W)", fontsize = 20)
ax1.set_title('Power generated over worst, best, nominal case orbits', fontsize = 30, pad=20)
plt.savefig("test2.png")
#%%

# =============================================================================
# Getting data for sunlight exposure to panels (this part is standalone from upper chunks, just run numpy)
# =============================================================================

orbit_length = 93 #Length of orbit in minutes approx
chunksize = orbit_length

dim = (orbit_length, 1)
port_orbit_sunlit = np.zeros(dim)

port_sunlit = []


# Summing the sunlight and dividing it by one orbit length for fraction of sunlight exposure
for chunk in pd.read_csv(folder_path +"EX2-Port-Power.csv", chunksize=chunksize):
    port_orbit_sunlit=(chunk.iloc[:,2])
    try:
        port_sunlit.append(sum(port_orbit_sunlit)/orbit_length)
    except:
        pass

orbit_total_sun = len(port_sunlit)
orbit_count_to_day = orbit_length/60/24
days_total_sun = orbit_total_sun * orbit_count_to_day


#%%

# =============================================================================
# Displaying sunlight exposure data
# =============================================================================

font = {'family' : 'serif',
        'sans-serif' : 'helvetica',
        'size'   : 20}

plt.rc('font', **font)

fig = plt.figure(figsize=(16, 4), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

ax1 = plt.subplot(1,1,1)
ax1.plot(np.linspace(0,days_total_sun,orbit_total_sun), 1-np.array(port_sunlit),linewidth = 3, color ='dodgerblue',label='Port')
ax1.set_xlim([0,364])
#ax1.set_ylim([0.6, 0.65])

ax1.set_xlabel('Time (Day)', fontsize = 25)
ax1.set_ylabel('Fraction of Orbital \n Time in Umbra (a.u.)', fontsize = 25)
ax1.set_title('Orbits by fractional sunlight exposure', fontsize = 30, pad=20)
plt.savefig("test.png")
