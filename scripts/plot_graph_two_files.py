import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
import sys

class DataManager:
	def __init__(self, leftFile, rightFile):
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
		self.fig = plt.figure(name)

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




if __name__ == "__main__":
	assert(len(sys.argv) > 2)
	datamanager = DataManager(sys.argv[1], sys.argv[2])

	for arm in datamanager.arms:
		x_c = arm.currentPoses[0][:]
		y_c = arm.currentPoses[1][:]
		z_c = arm.currentPoses[2][:]

		x_t = arm.targetPoses[0][:]
		y_t = arm.targetPoses[1][:]
		z_t = arm.targetPoses[2][:]

		fig = plt.figure(arm.name)
		ax = fig.add_subplot(311)
		ax.plot(arm.time, x_c, label="Robot Position")
		ax.plot(arm.time, x_t, label="Target Position")
		plt.ylabel("x")
		ax.legend()
		ax2 = fig.add_subplot(312)
		ax2.plot(arm.time, y_c, label="Robot Position")
		ax2.plot(arm.time, y_t, label="Target Position")
		plt.ylabel("y")
		ax2.legend()
		ax3 = fig.add_subplot(313)
		ax3.plot(arm.time, z_c, label="Robot Position")
		ax3.plot(arm.time, z_t, label="Target Position")
		ax3.legend()
		plt.ylabel("z")
		plt.xlabel("Seconds")

		plt.figure(arm.name + "x")
		plt.plot(arm.time, x_c, label="Robot Position")
		plt.plot(arm.time, x_t, label="Target Position")
		plt.legend()
		plt.ylabel("x")
		plt.xlabel("Seconds")


		plt.figure(arm.name + "y")
		plt.plot(arm.time, y_c, label="Robot Position")
		plt.plot(arm.time, y_t, label="Target Position")
		plt.legend()
		plt.ylabel("y")
		plt.xlabel("Seconds")

		plt.figure(arm.name + "z")
		plt.plot(arm.time, z_c, label="Robot Position")
		plt.plot(arm.time, z_t, label="Target Position")
		plt.legend()
		plt.ylabel("z")
		plt.xlabel("Seconds")


	plt.show()