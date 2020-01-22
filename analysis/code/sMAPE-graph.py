from helper import *
from numpy import *
from pathlib import Path
import matplotlib.pyplot as plt


for resolution in resolutions:
    path = "../results/" + resolution + "/average_sMAPE.csv"
    if Path(path).is_file():
        with open(path) as file:
            coefficients = [float(i) for i in file.readline().split(",")]
            plt.plot(range(1, len(coefficients)+1), coefficients, label=resolution)
plt.xlabel("Timestep after last observed value")
plt.ylabel("Average sMAPE")
plt.legend(loc='best')
plt.savefig("../results/sMAPE.png")
plt.show()
