import matplotlib.pyplot as plt
import pandas as pd



def graph(table):
    with open(table) as file:
        content = pd.read_csv(file)
        mx = content["mx ()"]
        my = content["my ()"]
        B_extx = content["B_extx (T)"]
        time_ns = content["# t (s)"]
        print(time_ns)
        
        #len(mx), for index, to select last element, len(mx)-1

        csfont = {"fontname":"Times New Roman"}
        
        plt.xlabel("Time (ns)", fontsize=15, **csfont)
        plt.ylabel("mx/my", fontsize=15, **csfont)
        plt.title("Ellipse", fontsize=20, **csfont)

        
        plt.plot(time_ns, mx, color="b", label="mx")
        plt.plot(time_ns, my, color="r", label="my")
        plt.legend()
        plt.show()



graph("Research_table_data.csv")
