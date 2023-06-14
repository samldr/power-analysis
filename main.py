import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from os import walk, mkdir
# from sys import stdout
from datetime import datetime,timezone

# =============================================================================
# Loads and initialzes data from csv files
# =============================================================================

# TODO: auto detect orbit period
# TODO: auto process the csv that stk outputs

now = datetime.now(timezone.utc) # get the time to name the files, also to see how long analysis takes

# initializes variables
orbit_length = 93 #int(input("mins per orbit: \n"))  # minutes per orbit
csv_files = [] 
dim = (orbit_length, 1)
chunksize = orbit_length

# set up input and output
path = "./csv/"
output_path = "./" + now.strftime("%Y%m%d-%H%M%S")
mkdir(output_path)
# stdout = open(output_path + '/report.txt', 'wt')
# print("test")


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

    file["energy"] = np.array(energy_list) # energy is integ
    file["power"] = np.array(power_list) # raw power (power grouped into orbits by minute)
    file["intensity"] = np.array(intensity_list) # intensity (grouped into orbits by minute)

total_energy = np.zeros(csv_files[0]["energy"].shape)
total_power = np.zeros(csv_files[0]["energy"].shape)

for file in csv_files:
    for idx, energy in enumerate(file["energy"]):
        total_power[idx] += (energy / orbit_length) # divide energy by time to get watts
        total_energy[idx] += (energy / 60) # convert energy to watt hours

# dataend = int(np.floor(len(total_power)/2)) # I'm not sure why this is here but it made it work for EX2 stuff
dataend = -1 # for everything else

print("\n==== Power Generated per Orbit ====")

# finds the max, min, and mean energy, along with their indexes
emax = total_energy[0:dataend].max()
emax_idx = np.where(total_energy[0:dataend] == emax)[0]
emin = total_energy[0:dataend].min()
emin_idx = np.where(total_energy[0:dataend] == emin)[0]
emean = total_energy[0:dataend].mean()
emean_idx = int(min(total_energy[0:dataend], key=lambda n : abs(n - emean))) # finds the index of the closest value to the mean

print("Max Energy: " + str(round(emax,2)) + " Wh")
print("Min Energy: " + str(round(emin,2)) + " Wh")
print("Mean Energy: " + str(round(emean,2)) + " Wh\n")

# find the max, min, and mean power, along with their indexes
pmax = total_power[0:dataend].max()
pmax_idx = np.where(total_power[0:dataend] == pmax)[0]
pmin = total_power[0:dataend].min()
pmin_idx = np.where(total_power[0:dataend] == pmin)[0]
pmean = total_power[0:dataend].mean()

print("Min Power: " + str(round(pmin, 2)) + " W")
print("Mean Power: " + str(round(pmean, 2)) + " W")
print("Max Power: " + str(round(pmax,2)) + " W\n")

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
plt.savefig(output_path + "/power_gen_per_orbit.png")
# plt.show()


# =============================================================================
# Fractional Sunlight Exposure
# =============================================================================
print("==== Fractional Sunlight Exposure ====")
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

fig = plt.figure(figsize=(16, 8), frameon=True)
plt.subplots_adjust(hspace=0.0)
fig.set_facecolor('w')

ax1 = plt.subplot(1,1,1)
ax1.plot(np.linspace(0,days_total_sun,orbit_total_sun), 1-np.array(sunlight),linewidth = 3, color ='dodgerblue',label='Total')
ax1.plot(np.linspace(0,days_total_sun,orbit_total_sun), (mean := 1 - np.array(sunlight).mean())*straight_line ,color = "limegreen", linestyle = "--", linewidth = 3,label='Mean')
ax1.legend(loc=0, fontsize = 20, ncol = 3)
ax1.set_xlim([0, days_total_sun])
ax1.set_ylim([0, 0.65])

ax1.set_xlabel('Time (Days)', fontsize = 25)
ax1.set_ylabel('Fraction of Orbital \n Time in Umbra (a.u.)', fontsize = 25)
ax1.set_title('Orbits by Fractional Sunlight Exposure', fontsize = 30, pad=20)
plt.savefig(output_path + "/fractional_sunlight_exposure.png")
print("Mean percentage of time in Umbra: " + str(round(mean * 100, 3)) + "%")



# =============================================================================
# Displaying Power generated over worst and best case orbits
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
for file in csv_files:
    ax1.plot(np.linspace(0, orbit_length, orbit_length), np.transpose(file["power"][emin_idx]), linewidth = 2, label = file["name"][:-4])
ax1.legend(loc=1, fontsize = 17, ncol = 3)
ax1.set_ylim([-0.5, 9.5])

ax2 = plt.subplot(3,1,2)
for file in csv_files:
    ax2.plot(np.linspace(0, orbit_length, orbit_length), np.transpose(file["power"][emax_idx]), linewidth = 2, label = file["name"][:-4])
# ax2.legend(loc=0, fontsize = 20, ncol = 3)
ax2.set_ylim([-0.5,9.5])

ax3 = plt.subplot(3,1,3)
for file in csv_files:
    ax3.plot(np.linspace(0, orbit_length, orbit_length), np.transpose(file["power"][emean_idx]), linewidth = 2, label = file["name"][:-4])
#ax2.legend(loc=0, fontsize = 20, ncol = 3)
ax2.set_ylim([-0.5,9.5])

ax3.set_xlabel('Time (Minute)', fontsize = 25)
ax1.set_ylabel(r"Power$_\mathrm{min}$ (W)", fontsize = 20)
ax2.set_ylabel(r"Power$_\mathrm{max}$ (W)", fontsize = 20)
ax3.set_ylabel(r"Power$_\mathrm{mean}$ (W)", fontsize = 20)
ax1.set_title('Power Generated Over Worst, Best, Nominal Case Orbits', fontsize = 30, pad=20)
plt.savefig(output_path + "/power_gen_worst_best_nominal.png")

print("\n")
print("Anaylsis finished in " + str(round((datetime.now(timezone.utc) - now).total_seconds(), 1)) + " seconds\n")