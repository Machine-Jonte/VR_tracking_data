from matplotlib.mlab import psd, csd
import csv 
import matplotlib.pyplot as plt
import numpy as np

def tfe(x, y, *args, **kwargs):
   """estimate transfer function from x to y, see csd for calling convention"""
   return csd(y, x, *args, **kwargs)[0] / psd(x, *args, **kwargs)[0]


if __name__ == "__main__":
    file = open("sweepsine_left.csv", "r")
    reader = csv.reader(file)
    t = []
    y = []
    x = []
    for line in reader:
        t.append(float(line[0]))
        y.append(float(line[1]))
        x.append(float(line[2]))
    # plt.plot(t, x)
    # plt.plot(t, y)

    frf = tfe(x,y)
    plt.semilogy(frf)
    plt.plot([0.6872]*len(frf))
    plt.show()