import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_directory = "C:/Users/Wayne&May/Downloads/Research_table_data.csv"

#set font

def graph(table):
    with open(table) as file:
        content = pd.read_csv(file)
        #mx = content["mx ()"]
        #B_extx = content["B_extx (mT)"]
        
        time = content["# t (s)"]
        energy_zee = content["E_Zeeman (J)"]
        energy_total = content["E_total (J)"]
        
        #len(mx), for index, to select last element, len(mx)-1

        csfont = {"fontname":"Times New Roman"}
        
        plt.xlabel("time (ns)", fontsize=15, **csfont)
        plt.ylabel("Zeeman energy", fontsize=15, **csfont)
        plt.title("Square", fontsize=20, **csfont)
        #plt.axvline(x = 0, color = 'k', label = 'axvline - full height')
        #plt.axhline(y = 0, color = 'k', linestyle = '-')




        
        plt.plot(time, energy_zee, "-x", color="b")
        plt.show()



graph("Research_table_data.csv")




