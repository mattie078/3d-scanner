from ConvertToPly import ConvertToPly
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import os


class Integratie:
	
	def __init__(self):
		self.RadiusThetaPhi = []  # waarom moeilijk doen als het ook makkelijk kan
		self.XYZ = []

	def ReadFile(self):
		hoek = 12
		sinus_hoek = np.sin(np.deg2rad(hoek))

		for i in range(0, 73):
			path = '..\\xycoordinates\\list' + str(i) + '.txt'
			data_array = np.loadtxt(fname=path)
			phi = (360./73.)*i

			for j in range(len(data_array)-1):
				radius = math.sqrt(float(data_array[j][1]/sinus_hoek)**2+float(data_array[j][0])**2)
				theta = np.arctan(float(data_array[j][0])/float(data_array[j][1]))
				self.RadiusThetaPhi.append([radius, theta, phi])

	def CalculateXYZ(self): #function for calculation of X,Y,Z from R,theta,phi

		rthetaphi = self.RadiusThetaPhi
		for i in range(len(rthetaphi)):
			r = rthetaphi[i][0]
			theta = rthetaphi[i][1]
			phi = rthetaphi[i][2]
			xVal = r * np.sin(theta) * np.cos(phi)
			yVal = r * np.sin(theta) * np.sin(phi)
			zVal = r * np.cos(theta)
		self.XYZ.append([xVal, yVal, zVal])
		
		ConverteerNaarPly(self.XYZ)


this = Intergratie
this.ReadFile()
this.CalculateXYZ()
