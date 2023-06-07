import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import integrate
from os import walk

# =============================================================================
# Loads and initialzes data from csv files
# =============================================================================

orbit_length = 43 #int(input("mins per orbit: \n"))  # minutes per orbit
csv_files = [] 
dim = (orbit_length, 1)
chunksize = orbit_length

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


for file in csv_files:
    temp_list = np.zeros(dim)
    power_list = intensity_list = energy_list =[]

    for orbit in pd.read_csv("./csv/" +  file["name"], chunksize=chunksize):
        temp_list = (orbit.iloc[:,1])

        if len(temp_list) == orbit_length:
            energy_list.append(integrate.cumtrapz(temp_list,np.linspace(0,orbit_length-1,orbit_length), initial=0)[-1])
            power_list.append(temp_list)
            #intensity_list.append((orbit.iloc[:,2]))

    
    print(energy_list)

    sfa = np.array(energy_list)
    #file["power"] = np.array(power_list[1:])
    #file["intensity"] = np.array(intensity_list[1:])

    # print(file)




print("done")