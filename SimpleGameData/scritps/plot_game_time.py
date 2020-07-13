import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from math import sqrt, pow
import colors

PATH = "../game_data/"

file_paths = ["expert", "expertCM", "1", "1CM", "2", "2CM", "3", "3CM", "4", "4CM", "5", "5CM", "6", "7", "7CM", "8", "8CM", "9", "9CM", "10", "10CM"]

dots = ["o", "s"] + ["o","s"] + ["o", "s"] + ["o","s"] + ["o", "s"] + ["o", "s"] + ["o"] + ["o", "s"] + ["o", "s"] + ["o", "s"] + ["o", "s"]
cmap = colors.get_cmap(len(dots))
coords = [0.9,1.1, 1.9,2.1, 2.9,3.1, 3.9,4.1, 4.9, 5.1, 5.9,6.1, 7, 7.9,8.1, 8.9,9.1, 9.9,10.1, 10.9,11.1]
colors = [cmap(0)]*2 + [cmap(1)]*2 + [cmap(2)]*2 + [cmap(3)]*2 + [cmap(4)]*2 + [cmap(5)]*2 + [cmap(6)] + [cmap(7)] *2 + [cmap(8)]*2 + [cmap(9)]*2 + [cmap(10)]*2

def meanAndSd(player_time):
    mean = float(sum(player_time)/len(player_time))
    sd = sqrt( 1.0/float(len(player_time)) * sum([pow(float(x)-mean,2) for x in player_time]) )

    return mean, sd

if __name__=="__main__":
    game_data = []

    
    for file_path in file_paths:
        user_data = []
        files = [f for f in listdir(PATH + file_path) if isfile(join(PATH + file_path, f))]
        files.sort()
        for file in files:
            # The structure of the matrix is time, score, left position, left target position, right position, right target position
            # matrix of size 6
            user_data.append(np.loadtxt(PATH + file_path + "/" + file, delimiter=',', usecols=range(6), dtype=np.float32))
        game_data.append(user_data)

    player_times = []
    for user_data in game_data:
        player_times.append([matrix[-1,0] for matrix in user_data])


    lables = file_paths
    sums = []
    for i, player_time in enumerate(player_times):
        plt.figure(1)
        plt.plot(range(1,8),player_time, dots[i]+'--', dashes=(1, 1), label=lables[i], color=colors[i])
        plt.figure(2)
        mean, sd = meanAndSd(player_time)
        plt.errorbar(coords[i], mean, sd, linestyle='None', marker=dots[i], label=lables[i], color=colors[i])
        
    plt.figure(1)
    plt.ylabel("Seconds")
    plt.xlabel("Game instance/random seed")
    plt.axis([0,8,0,500])
    plt.legend()
    plt.figure(2)
    plt.ylabel("Seconds")
    plt.xlabel("Players")
    # plt.legend()
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])

    plt.show()