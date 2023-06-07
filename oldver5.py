import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from os import walk

# =============================================================================
# Loads and initialzes data from csv files
# =============================================================================

orbit_length = input("mins per orbit: ")  # minutes per orbit
csv_files = [] 

# initializes an empty object for each file in ./csv
for root, dirs, files in walk("./csv", topdown = True):
    for file in files:
        if file.endswith(".csv"):
            csv_files.append(
                {
                "name": file,
                "power": [],
                "intensity": [],
                "energy": [],
                })

# gets the power, intensity and energy data from the sheets per orbit and puts it in the object
# energy per orbit is found by integrating power over one orbit
for file in csv_files:
    for orbit in pd.read_csv("./csv/" +  file["name"], chunksize = orbit_length):
        p_list = (orbit.iloc[:,1])
        try:
            file["energy"].append(integrate.cumulative_trapezoid(p_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
            file["power"].append(p_list)
            file["intensity"].append((orbit.iloc[:,2]))
        except:
            pass

        # try:
        #     file["power"].append(power := (orbit.iloc[:,1]))
        #     file["intensity"].append((orbit.iloc[:,2])) # this can probably be optimized
        #     file["energy"].append((integrate.cumulative_trapezoid(power, np.linspace(0, orbit_length - 1, orbit_length), initial = 0)[-1])) # same as V4
        # except:
        #     pass

    # converts the data to numpy arrays so it can be used by other modules. theres probably a better way of doing this

    # print("power length: " + str(len(file["power"])))
    # print("energy length: " + str(len(file["energy"])))
    # print("")


    # print("")
    # print(file["power"])
    # print(type(file["power"]))
    # print(file["energy"])
    # print(type(file["energy"]))
    

    file["power"] = np.asarray(file["power"])
    file["intensity"] = np.asarray(file["intensity"])
    file["energy"] = np.asarray(file["energy"])

    # print("")
    # print(file["power"])
    # print(type(file["power"]))
    # print(file["energy"])
    # print(type(file["energy"]))

#print("csv files loaded")

# print("power length: " + str(len(csv_files[0]["power"])))
# print("energy length: " + str(len(csv_files[0]["energy"])))
# print("")

# print(csv_files[0]["power"])
# print(type(csv_files[0]["power"]))
# print("")
# print(csv_files[0]["energy"])
# print(type(csv_files[0]["energy"]))

# # =============================================================================
# # Analysis
# # =============================================================================

# # gets the total energy of all panels (in Wh) and the total power of all panels (in W)

total_energy = np.zeros(csv_files[0]["energy"].shape)
total_power = np.zeros(csv_files[0]["power"].shape)

# power_array = ([i["power"]] for i in csv_files) 
# print(power_array)

# total_power = np.divide((np.add(i["power"]) for i in csv_files), orbit_length)
# total_energy = np.divide((np.add(i["energy"]) for i in csv_files), 60)


for idx, file in enumerate(csv_files):
    total_energy += (file["energy"] / 60) 
    
    total_power += file["power"] / orbit_length

# # csv_files["power"] 

print(total_energy)
print(total_power)

# #for file in csv_files:
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



# # #emean_orbit = (port_list[:,99].mean()+port_dep_list[:,99].mean()+star_list[:,99].mean()+star_dep_list[:,99].mean()+zenith_list[:,99].mean())
# # print("Min, idx: " + str(emin) + ", " + str(emin_idx))
# # print("Mean, idx: " + str(emean) + ", " + str(emean_idx))
# # print("Max, idx: " + str(emax) + ", " + str(emax_idx))
# # #print("Mean Power: " + str(emean_orbit))

# # print("Min, idx: " + str(pmin) + ", " + str(pmin_idx))
# # print("Mean, idx: " + str(pmean) + ", " + str(pmean_idx))
# # print("Max, idx: " + str(pmax) + ", " + str(pmax_idx))


# #%%
# # =============================================================================
# # Displaying Power Generated Per Orbit of ExAlta 2
# # =============================================================================

# # declaring variable sizes for plotting
# orbit_total = len(csv_files[0]["power"])
# orbit_count_to_day = orbit_length/60/24
# days_total = orbit_total * orbit_count_to_day
# straight_line = np.ones(orbit_total)

# font = {'family' : 'serif',
#         'sans-serif' : 'helvetica',
#         'size'   : 20}

# plt.rc('font', **font)

# fig = plt.figure(figsize=(16, 8), frameon=True)
# plt.subplots_adjust(hspace=0.0)
# fig.set_facecolor('w')

            
# ax1 = plt.subplot(1,1,1)

# #for file in csv_files:
# #    ax1.plot(np.linspace(0,days_total,orbit_total),file["power"]/orbit_length, color = 'dodgerblue', linewidth = 2, label=file["name"])

# ax1.plot(np.linspace(0,days_total,orbit_total),csv_files[0]["power"],linestyle = "--",linewidth = 2, color ='dodgerblue',label=csv_files[0]["name"])
# ax1.plot(np.linspace(0,days_total,orbit_total),csv_files[1]["power"],linestyle = "--",linewidth = 2,color ='blue',label=csv_files[1]["name"])
# ax1.plot(np.linspace(0,days_total,orbit_total),csv_files[2]["power"],linestyle = "--",linewidth = 2,color ='red',label=csv_files[2]["name"])
# ax1.plot(np.linspace(0,days_total,orbit_total),csv_files[3]["power"],linestyle = "--",linewidth = 2,color ='darkred',label=csv_files[3]["name"])
# ax1.plot(np.linspace(0,days_total,orbit_total),csv_files[4]["power"],linestyle = "--", linewidth = 2,color ='darkviolet',label=csv_files[4]["name"])
# ax1.plot(np.linspace(0,days_total,orbit_total),pmax*straight_line,'darkgreen', linestyle ='--',linewidth = 2,label='Max')
# ax1.plot(np.linspace(0,days_total,orbit_total),pmin*straight_line,'chartreuse', linestyle ='--',linewidth = 2,label='Min')
# ax1.plot(np.linspace(0,days_total,orbit_total),pmean*straight_line,'limegreen', linestyle ='--',linewidth = 2,label='Mean')
# ax1.plot(np.linspace(0,days_total,orbit_total),total_power,linewidth = 2,color = 'k',label='Total')
# ax1.plot(np.linspace(0,days_total,orbit_total),pmax*straight_line,'darkgreen', linestyle ='--',linewidth = 2,label='Max')

# #for when port and starboard are 0
# # ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='red',label='Port')
# # ax1.plot(np.linspace(0,days_total,orbit_total),straight_line*0,linewidth = 2,color ='darkred',label='Starboard')

# #ax1.legend(loc=0, fontsize = 20, ncol = 3)
# ax1.set_xlim([0,364])
# ax1.set_ylim([-.5, 9])

# ax1.set_xlabel('Time (Day)', fontsize = 25)
# ax1.set_ylabel('Power (W)', fontsize = 25)
# ax1.set_title('Power generated per orbit of ExAlta 2', fontsize = 30, pad=20)
# plt.savefig("test4.png")





