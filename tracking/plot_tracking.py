import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
import sys
import matplotlib.patches as mpatches

class DataManager:
	def __init__(self, leftFile="left_tracking.csv", rightFile="right_tracking.csv"):
		files = [open(leftFile, "r"), open(rightFile, "r")]
		self.arms = [  ArmData(files[0], "left"),    # left
					   ArmData(files[1], "right")  ] # right

class ArmData:
	def __init__(self, file, name):
		self.currentPoses = [] # 3 rows (x,y,z) x N column
		self.targetPoses = [] # 3 rows (x,y,z) x N column
		self.time = []
		self.readFile(file)
		self.name = name

	def readFile(self, file):
		x_t = []
		y_t = []
		z_t = []
		x_c = []
		y_c = []
		z_c = []


		reader = csv.reader(file)
		for i, line in enumerate(reader):
			if i == 0:
				continue
			self.time.append(float(line[0]))
			# Target pose
			x_t.append(float(line[1]))
			y_t.append(float(line[2]))
			z_t.append(float(line[3]))
			# self.targetPoses.append([line[1], line[2], line[3]])
			# Current pose
			x_c.append(float(line[4]))
			y_c.append(float(line[5]))
			z_c.append(float(line[6]))
			# self.currentPoses.append([line[4], line[5], line[6]])
		
		self.currentPoses = [x_c, y_c, z_c]
		self.targetPoses = [x_t, y_t, z_t]

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
	datamanager = DataManager()
	if len(sys.argv) > 2:
		datamanager = DataManager(sys.argv[1], sys.argv[2])
		
	for arm in datamanager.arms:
		x_c = arm.currentPoses[0][:]
		y_c = arm.currentPoses[1][:]
		z_c = arm.currentPoses[2][:]

		x_t = arm.targetPoses[0][:]
		y_t = arm.targetPoses[1][:]
		z_t = arm.targetPoses[2][:]

		fig = plt.figure(arm.name)
		ax = fig.add_subplot(111, projection='3d')
		ax.plot(x_c, y_c, z_c, label="Robot End Effector Path")
		ax.plot(x_t, y_t, z_t, label="Processed Controller Path")
		ax.set_xlabel('X axis')
		ax.set_ylabel('Y axis')
		ax.set_zlabel('Z axis')
		ax.legend()
		ax.set_aspect('equal')
		set_axes_equal(ax)
		# ax.set_xlim(0, 1)
		# ax.set_ylim(0, 1)
		# ax.set_zlim(0, 1)
		# plt.figure("diagram_" + arm.name)
		# bar_names = ["x", "y", "z"]
		# bars = [abs(np.sum(x_t)-np.sum(x_c)), 
		# 		abs(np.sum(y_t)-np.sum(y_c)),
		# 		abs(np.sum(z_t)-np.sum(z_c))]
		# # print(np.sum(x_c))
		# # print(np.sum(x_t))
		# plt.bar(bar_names,bars)
	plt.show()
