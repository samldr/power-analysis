import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from os import walk
from datetime import datetime,timezone

# =============================================================================
# Loads and initialzes data from csv files
# =============================================================================

# TODO: auto detect orbit period
orbit_length = 93 #int(input("mins per orbit: \n"))  # minutes per orbit
csv_files = [] 
dim = (orbit_length, 1)
chunksize = orbit_length
path = "./csv/"
now = datetime.now(timezone.utc)

# initializes an empty object for each file in ./csv/
for root, dirs, files in walk(path, topdown = True):
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(
                {
                "name": file,
                "power": [],
                "intensity": [],
                "energy": [],
                })
            print('Loaded ' + file)


# retrieves the power and intensity data from the csv files
# computes energy by integrating power over each orbit
for file in csv_files:
    
    temp_list = np.zeros(dim)
    energy_list = []
    power_list = []
    intensity_list = []

    for orbit in pd.read_csv(path +  file["name"], chunksize=chunksize):
        temp_list = (orbit.iloc[:,1].to_list())

        try:
            energy_list.append(integrate.cumulative_trapezoid(temp_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
            power_list.append(temp_list)
            intensity_list.append((orbit.iloc[:,2].to_list()))
        except:
            pass

    # print("")
    # print(energy_list)

    file["energy"] = np.array(energy_list) # energy is power times orbit_length
    file["power"] = np.array(power_list) # raw power (power grouped into orbits by minute)
    file["intensity"] = np.array(intensity_list) # intensity (grouped into orbits by minute)
   
# print(csv_files)

total_energy = np.zeros(csv_files[0]["energy"].shape)
total_power = np.zeros(csv_files[0]["energy"].shape)

for file in csv_files:
    for idx, energy in enumerate(file["energy"]):
        total_power[idx] += (energy / orbit_length) # divide energy by time to get watts
        total_energy[idx] += (energy / 60) # convert energy to watt/s (joules)

dataend = int(np.floor(len(total_power)/2)) # I'm not sure why this is here but it makes it work?

emax = total_energy[0:dataend].max()
emax_idx = np.where(total_energy[0:dataend] == emax)[0]
emin = total_energy[0:dataend].min()
emin_idx = np.where(total_energy[0:dataend] == emin)[0]
emean = total_energy[0:dataend].mean()

# print([emax, emax_idx])
# print([emin, emin_idx])
# print(emean)
# print("")

pmax = total_power[0:dataend].max()
pmax_idx = np.where(total_power[0:dataend] == pmax)[0]
pmin = total_power[0:dataend].min()
pmin_idx = np.where(total_power[0:dataend] == pmin)[0]
pmean = total_power[0:dataend].mean()

# print([pmax, pmax_idx])
# print([pmin, pmin_idx])
# print(pmean)
# print("")

# print(total_energy)
# print(total_power)

# =============================================================================
# Power Generated Per Orbit
# =============================================================================

# declaring variable sizes for plotting
orbit_total = len(total_power)
orbit_count_to_day = orbit_length / 1440
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

for file in csv_files:
    ax1.plot(np.linspace(0, days_total, orbit_total), file["energy"] / orbit_length, linewidth = 2, label = file["name"][:-4])

ax1.plot(np.linspace(0,days_total,orbit_total), pmax * straight_line, 'darkgreen', linestyle ='--', linewidth = 2, label = 'Max')
ax1.plot(np.linspace(0,days_total,orbit_total), pmin * straight_line, 'chartreuse', linestyle ='--', linewidth = 2, label = 'Min')
ax1.plot(np.linspace(0,days_total,orbit_total), pmean * straight_line, 'limegreen', linestyle ='--', linewidth = 2, label = 'Mean')
ax1.plot(np.linspace(0,days_total,orbit_total), total_power, linewidth = 2, color = 'k', label = 'Total')

ax1.legend(loc=0, fontsize = 20, ncol = 3)
ax1.set_xlim([0,364])
ax1.set_ylim([-.5, 9])

ax1.set_xlabel('Time (Days)', fontsize = 25)
ax1.set_ylabel('Power (W)', fontsize = 25)
ax1.set_title('Power Generated per Orbit', fontsize = 30, pad=20)
plt.savefig(now.strftime("%Y%m%d-%H%M%S") + "-PGPO")
# plt.show()


# =============================================================================
# Fractional Sunlight Exposure
# =============================================================================

sunlight = []
#sunlight_np = np.zeros(len(csv_files[0]["intensity"]))
for intensity in csv_files[0]["intensity"]:
    sunlight.append(sum(intensity)/orbit_length)
    
#sunlight_np = np.array(sunlight)

orbit_total_sun = len(sunlight)
orbit_count_to_day = orbit_length/60/24
days_total_sun = orbit_total_sun * orbit_count_to_day

font = {'family' : 'serif',
        'sans-serif' : 'helvetica',
        'size'   : 20}

plt.rc('font', **font)

fig = plt.figure(figsize=(16, 6), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

ax1 = plt.subplot(1,1,1)
ax1.plot(np.linspace(0,days_total_sun,orbit_total_sun), 1-np.array(sunlight),linewidth = 3, color ='dodgerblue',label='Satellite')
# ax1.plot(np.linspace(0,days_total_sun,orbit_total_sun), linewidth = 3, color ='dodgerblue',label='Satellite')
ax1.set_xlim([0,364])
ax1.set_ylim([0, 0.65])

ax1.set_xlabel('Time (Days)', fontsize = 25)
ax1.set_ylabel('Fraction of Orbital \n Time in Umbra (a.u.)', fontsize = 25)
ax1.set_title('Orbits by Fractional Sunlight Exposure', fontsize = 30, pad=20)
plt.savefig(now.strftime("%Y%m%d-%H%M%S") + "-FSE")

print("Anaylsis finished in " + str((datetime.now(timezone.utc) - now).total_seconds()) + " seconds")