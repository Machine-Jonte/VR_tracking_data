import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
import sys
import matplotlib.patches as mpatches
import pandas as pd
from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons


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


def plotTrajectory(x, y, z, name, label=""):
    fig = plt.figure(name)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=label)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    ax.set_aspect('equal')
    set_axes_equal(ax)

def plotDubbelTrajectory(x, y, z, x2, y2, z2, name, label=["", ""]):
    fig = plt.figure(name)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=label[0])
    ax.plot(x2, y2, z2, label=label[1])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    ax.set_aspect('equal')
    set_axes_equal(ax)


class AlterablePlot:
    def __init__(self, name, mean_shape, pca):
        self.fig, self.ax = plt.subplots()
        self.ax2 = self.fig.add_subplot(111, projection='3d')
        plt.subplots_adjust(left=0.0, bottom=0.0, top=1, right=0.5)
        self.axcolor = 'lightgoldenrodyellow'
        # self.axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=self.axcolor)
        # self.axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=self.axcolor)
        self.components = np.zeros((pca.n_components_, 1))

        self.axcomp = [plt.axes([0.5, float(i) * 0.9/float(self.components.size)+0.1, 0.5, 0.8/float(self.components.size)], facecolor=self.axcolor) for i in range(self.components.size)]

        self.mean_shape = mean_shape
        self.pca = pca

        self.components_slider = [Slider(self.axcomp[i], "c" + str(i+1), -500.0, 500.0, valinit=self.components[i], valstep=0.1) for i in range(self.components.size)]
        for slider in self.components_slider:
            slider.on_changed(self.update)
        
        self.resetax = plt.axes([0.70, 0.025, 0.1, 0.04])
        self.button = Button(self.resetax, 'Reset', color=self.axcolor, hovercolor='0.975')
        self.button.on_clicked(self.reset)

        self.visibility = [True, True, True, True]
        self.update(0)

        # Make checkbuttons with all plotted lines with correct visibility
        rax = plt.axes([0.05, 0.80, 0.20, 0.15])
        self.labels = [str(line.get_label()) for line in self.lines]
        self.visibility = [line.get_visible() for line in self.lines]
        self.check = CheckButtons(rax, self.labels, self.visibility)
        self.check.on_clicked(self.checkFunction)

    def reset(self, event):
        [slider.reset() for slider in self.components_slider]

    def checkFunction(self, label):
        index = self.labels.index(label)
        self.lines[index].set_visible(not self.lines[index].get_visible())
        self.visibility[index] = not self.visibility[index]
        plt.draw()

    # def plot(self, x, y, z, label=""):
    #     # ax = self.fig.add_subplot(111, projection='3d')
    #     self.ax2.plot(x, y, z, label=label)

    def update(self, val):
        self.ax2.cla()
        self.components = np.array([slider.val for slider in self.components_slider])
        new_shape = self.mean_shape + np.dot(self.pca.components_.T, self.components)
        new_shape = new_shape.flatten()

        self.l1, = self.ax2.plot(new_shape[0:50], new_shape[50:100], new_shape[100:150],                       label="Left PCA"  , visible=self.visibility[0])
        self.l2, = self.ax2.plot(new_shape[150:200], new_shape[200:250], new_shape[250:300],                   label="Right PCA" , visible=self.visibility[1])
        self.l3, = self.ax2.plot(self.mean_shape[0:50], self.mean_shape[50:100], self.mean_shape[100:150],     label="Left Mean" , visible=self.visibility[2])
        self.l4, = self.ax2.plot(self.mean_shape[150:200], self.mean_shape[200:250], self.mean_shape[250:300], label="Right Mean", visible=self.visibility[3])

        self.lines = [self.l1, self.l2, self.l3, self.l4]

        self.ax2.set_xlabel('X axis')
        self.ax2.set_ylabel('Y axis')
        self.ax2.set_zlabel('Z axis')
        self.ax2.legend()
        self.ax2.set_aspect('equal')
        set_axes_equal(self.ax2)
