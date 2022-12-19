import glob
from matplotlib import pyplot as plt
import numpy as np


DMI = []
current = []
switch = []


column_magnetic_number = 3

files = glob.glob("C:/Users/Wayne&May/Desktop/Simulation/*.out")
#print(files)

for file in files:
    file_name = file.split("/")[4]
    print(file_name)
    current_stenght = file_name.split("_")[5]
    #print(current_stenght)

    new_current = current_stenght.replace(".out", "")
    current.append(float(new_current))
    
    new_DMI = file_name.split("_")[3]
    DMI.append(float(new_DMI))
    
    with open(f"{file}/table.txt", "r") as data_file:
        data = np.loadtxt(data_file, skiprows=8001)

        c = 0
        for x in np.nditer(data):
            c += 1
            if c == 4:
                switch.append(x)

#take the absolute value
# = [abs(mag) for mag in magnetic]




#change color !!!!!!!
plt.scatter(DMI, current, c=switch, cmap=("Reds"), edgecolors="black", linewidths=1, s=100)

plt.xlabel("Magnetic (T)")
plt.ylabel("Current ($10^{11} A/m^2$)")

cbar = plt.colorbar()
cbar.set_label("switch")
plt.show()       
