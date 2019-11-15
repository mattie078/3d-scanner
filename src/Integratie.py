from ConverteerNaarPly import ConverteerNaarPly
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import os


class Integratie:

	def ReadFile(self):
		RadiusThetaPhi = []
		hoek = 12
		sinus_hoek = np.sin(np.deg2rad(hoek))

		for i in range(0, 73):
			path = '..\\temps\\xycoordinates\\tempXY' + str(i) + '.txt'
			data_array = np.loadtxt(fname=path)
			phi = (360./73.)*i

			for j in range(len(data_array)-1):
				radius = math.sqrt(float(data_array[j][1]/sinus_hoek)**2+float(data_array[j][0])**2)
				theta = np.arctan(float(data_array[j][0])/float(data_array[j][1]))
				RadiusThetaPhi.append([radius, theta, phi])

		XYZ = []

		for i in range(len(RadiusThetaPhi)):
			r = RadiusThetaPhi[i][0]
			theta = RadiusThetaPhi[i][1]
			phi = RadiusThetaPhi[i][2]
			xVal = r * np.sin(theta) * np.cos(phi)
			yVal = r * np.sin(theta) * np.sin(phi)
			zVal = r * np.cos(theta)
			XYZ.append([xVal, yVal, zVal])
		
		ConverteerNaarPly(XYZ)
