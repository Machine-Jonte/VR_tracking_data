import numpy as np
import scipy
import sklearn
from sklearn.decomposition import PCA
import pandas as pd
from os import listdir
from os.path import isfile, join
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import trackplot
from matplotlib.widgets import Slider, Button, RadioButtons
from sklearn import preprocessing
from scipy import stats
import sys


# PATH = "./two_circles/"
PATH = "./training/"
# PATH = "./complex/"



def shiftDataOrigin(matrix):
    # Return the mean for each input data in that coordinate
    # Example: 10 input files will return x_mean with 10 elements
    x_mean = (np.sum(matrix[:,0:50],    axis=1) + np.sum(matrix[:,150:200], axis=1))/100
    y_mean = (np.sum(matrix[:,50:100],  axis=1) + np.sum(matrix[:,200:250], axis=1))/100
    z_mean = (np.sum(matrix[:,100:150], axis=1) + np.sum(matrix[:,250:300], axis=1))/100

    # Move each data point to the origin. The difference between the arms are still kept!
    print(x_mean)
    matrix[:,0:50]    -= np.array([list(x_mean)]*50).T
    matrix[:,150:200] -= np.array([list(x_mean)]*50).T
    matrix[:,50:100]  -= np.array([list(y_mean)]*50).T
    matrix[:,200:250] -= np.array([list(y_mean)]*50).T
    matrix[:,100:150] -= np.array([list(z_mean)]*50).T
    matrix[:,250:300] -= np.array([list(z_mean)]*50).T

    return matrix


if __name__ == "__main__":
    if len(sys.argv) > 1:
        PATH = sys.argv[1]
    files = [f for f in listdir(PATH) if isfile(join(PATH, f))]
    print(files)
    matrix = []
    for file in files:
        df = pd.read_csv(PATH + file)
        # print(df.head())

        row = []
        names = ["left", "right"]
        for name in names:
            df_arm  = df.loc[:, df.columns.str.startswith(name) ]
            arm_array = df_arm.to_numpy()

            coords = []
            for i in range(3,6):
                coord_array = arm_array[:,i] 
                coord_interp = interp.interp1d(np.arange(coord_array.size), coord_array)
                coord_sized = coord_interp(np.linspace(0,coord_array.size-1,50))
                coords.append(coord_sized)
                # print(coord_sized.size)
                row += list(coord_sized)


            # trackplot.plotTrajectory(trajectory.x, trajectory.y, trajectory.z, trajectory.name)
            # plt.plot(coord_sized)
            # plt.show()
        matrix.append(row)
        # plt.show()


    # matrix = preprocessing.normalize(matrix, axis=1)
    matrix = np.array(matrix)
    matrix = shiftDataOrigin(matrix)
    # Flatten in the x-axis
    # for i in range(matrix.shape[0]):
    #     matrix[i,0:50] = 0
    #     matrix[i,150:200] = 0
    matrix = preprocessing.scale(matrix, axis=1)
    # matrix = stats.zscore(matrix)

    # matrix = np.array(matrix)
    
    trackplot.plotMatrix(matrix)

    data_matrix = np.array(matrix)
    pca = PCA(n_components=8)
    principle_components = pca.fit_transform(data_matrix)
    mean_shape = np.sum(data_matrix, axis=0)

    alterable_plt = trackplot.AlterablePlot("test", mean_shape, pca)
    plt.show()
