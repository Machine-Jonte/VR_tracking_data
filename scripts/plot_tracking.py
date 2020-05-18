import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
import sys
import matplotlib.patches as mpatches
import pandas as pd


# From (https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to)
def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''
    
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


if __name__ == "__main__":
    assert(len(sys.argv) > 1)
    df = pd.read_csv(sys.argv[1]) 

    df_left  = df.loc[:, df.columns.str.startswith("left" ) ]
    df_right = df.loc[:, df.columns.str.startswith("right") ]
    time     = df.loc[:, df.columns.str.startswith("time" ) ]

    # print(df_left[0])
    print(df_right.head()) 

    print(df_right.iloc[:,0])
    arms = [df_left, df_right]    
    names = ["left", "right"]

    for i, arm in enumerate(arms):
        x_t = arm.iloc[:,0]
        y_t = arm.iloc[:,1]
        z_t = arm.iloc[:,2]
    
        x_c = arm.iloc[:,3]
        y_c = arm.iloc[:,4]
        z_c = arm.iloc[:,5]
        
        fig = plt.figure(names[i])
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x_c, y_c, z_c, label="Robot End Effector Path")
        ax.plot(x_t, y_t, z_t, label="Processed Controller Path")
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.legend()
        ax.set_aspect('equal')
        set_axes_equal(ax)
    plt.show()
