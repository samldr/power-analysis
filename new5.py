import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from os import walk

# =============================================================================
# Loads and initialzes data from csv files
# =============================================================================

orbit_length = 93 #int(input("mins per orbit: \n"))  # minutes per orbit
csv_files = [] 
dim = (orbit_length, 1)
chunksize = orbit_length

# initializes an empty object for each file in ./csv
for root, dirs, files in walk("./csv_backup/", topdown = True):
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(
                {
                "name": file,
                "power": [],
                "intensity": [],
                "energy": [],
                })


for file in csv_files:
    
    temp_list = np.zeros(dim)
    energy_list = []
    power_list = []
    intensity_list = []

    for orbit in pd.read_csv("./csv_backup/" +  file["name"], chunksize=chunksize):
        temp_list = (orbit.iloc[:,1].to_list())
    
        if len(temp_list) == orbit_length:
            energy_list.append(integrate.cumtrapz(temp_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
            power_list.append(temp_list)
            intensity_list.append((orbit.iloc[:,2].to_list()))

    # print("")
    # print(energy_list)

    file["energy"] = np.array(energy_list)
    file["power"] = np.array(power_list)
    file["intensity"] = np.array(intensity_list)

   
# print(csv_files)

total_energy = np.zeros(csv_files[0]["energy"].shape)
total_power = np.zeros(csv_files[0]["power"].shape)

for file in csv_files:
    total_energy += file["energy"] / orbit_length 
    total_power += file["power"] / 60

# print(total_energy)
# print(total_power)


# =============================================================================
# Displaying Power Generated Per Orbit
# =============================================================================

# declaring variable sizes for plotting
orbit_total = len(total_power)
orbit_count_to_day = orbit_length/60/24
days_total = orbit_total * orbit_count_to_day
#straight_line = np.ones(orbit_total)

font = {'family' : 'serif',
        'sans-serif' : 'helvetica',
        'size'   : 20}

plt.rc('font', **font)

fig = plt.figure(figsize=(16, 8), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

            
ax1 = plt.subplot(1,1,1)

for file in csv_files:
    ax1.plot(np.linspace(0,days_total,orbit_total),file["energy"]/orbit_length, linewidth = 2, label=file["name"][:-4])

# ax1.plot(np.linspace(0,days_total,orbit_total),pmax*straight_line,'darkgreen', linestyle ='--',linewidth = 2,label='Max')
# ax1.plot(np.linspace(0,days_total,orbit_total),pmin*straight_line,'chartreuse', linestyle ='--',linewidth = 2,label='Min')
# ax1.plot(np.linspace(0,days_total,orbit_total),pmean*straight_line,'limegreen', linestyle ='--',linewidth = 2,label='Mean')
ax1.plot(np.linspace(0,days_total,orbit_total), total_energy, linewidth = 2, color = 'k', label='Total')

#for when port and starboard are 0
# ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='red',label='Port')
# ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='darkred',label='Starboard')

ax1.legend(loc=0, fontsize = 20, ncol = 3)
ax1.set_xlim([0,364])
ax1.set_ylim([-.5, 9])

ax1.set_xlabel('Time (Days)', fontsize = 25)
ax1.set_ylabel('Power (W)', fontsize = 25)
ax1.set_title('Power Generated per Orbit', fontsize = 30, pad=20)
plt.savefig("test4.png")


print("done")