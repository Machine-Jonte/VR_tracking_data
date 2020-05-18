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



PATH = "./training/"

class Trajectory:
    def __init__(self, name):
        self.name = name
        self.x = []
        self.y = []
        self.z = []

    def setCoordFromCoords(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]

if __name__ == "__main__":
    files = [f for f in listdir(PATH) if isfile(join(PATH, f))]
    print(files)
    matrix = []
    for file in files:
        df = pd.read_csv(PATH + file)
        # print(df.head())

        trajectories = [Trajectory("left"), Trajectory("right")]
        row = []
        for trajectory in trajectories:
            df_arm  = df.loc[:, df.columns.str.startswith(trajectory.name) ]
            arm_array = df_arm.to_numpy()

            coords = []
            for i in range(3):
                coord_array = arm_array[:,i] 
                coord_interp = interp.interp1d(np.arange(coord_array.size), coord_array)
                coord_sized = coord_interp(np.linspace(0,coord_array.size-1,50))
                coords.append(coord_sized)
                # print(coord_sized.size)
                row += list(coord_sized)

            trajectory.setCoordFromCoords(coords)

            # trackplot.plotTrajectory(trajectory.x, trajectory.y, trajectory.z, trajectory.name)
            # plt.plot(coord_sized)
            # plt.show()
        matrix.append(row)
        # plt.show()


    # matrix = preprocessing.normalize(matrix, axis=1)
    matrix = np.array(matrix)
    for i in range(matrix.shape[0]):
        matrix[i,0:50] = 0
        matrix[i,150:200] = 0
    matrix = preprocessing.scale(matrix, axis=1)

    # matrix = np.array(matrix)
    
    fig = plt.figure("all")
    ax = fig.add_subplot(111, projection='3d')
    for i in range(matrix.shape[0]):
        matrix[i,0:50] = 0
        matrix[i,150:200] = 0
        color = list(np.random.choice(np.arange(0,1,0.0001), size=3))
        ax.plot(matrix[i,0:50], matrix[i,50:100], matrix[i,100:150], label=str(i), color=color)
        ax.plot(matrix[i,150:200], matrix[i,200:250], matrix[i,250:300], label=str(i), color=color)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        # ax.legend()
        ax.set_aspect('equal')
        trackplot.set_axes_equal(ax)

    # matrix = stats.zscore(matrix)
    # matrix = preprocessing.scale(matrix)
    data_matrix = np.array(matrix)
    pca = PCA(n_components=10)
    principle_components = pca.fit_transform(data_matrix)

    # print(pca.n_components_)
    # print(principle_components.shape)
    # print(pca.components_.shape)

    mean_shape = np.sum(data_matrix, axis=0)

    new_shape = mean_shape + np.dot(pca.components_.T, np.array([0,0,0,0,0,0,0,0,0,0]))

    alterable_plt = trackplot.AlterablePlot("test", mean_shape, pca)
    plt.show()
