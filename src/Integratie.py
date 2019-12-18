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
		# RadiusThetaPhi = []
		XYZ = []
		hoek = 12  # Hoek in graden tussen de twee lasers als ze elkaar kruisen (op het middelpunt van het draaiplateau)
		sinus_hoek = np.sin(np.deg2rad(hoek))

		for i in range(0, 73):
			path = '..\\temps\\xycoordinates\\tempXY' + str(i) + '.txt'
			data_array = np.loadtxt(fname=path)
			phi = (360./73.)*i
			# Hier wordt de afstand tussen de lasers op elke hoogte omgezet in een bolcoördinaat.
			# De radius is de afstand tussen het middelpunt (van het draaiplateau) en het snijpunt met de linker laser.
			# Dit wordt berekend met de stelling van Pythagoras:
			# Radius = sqrt( (horizontale afstand)^2 + (verticale afstand)^2
			# De horizontale afstand is gelijk aan de afstand tussen de lasers gedeeld door de sinus van
			# de hoek tussen de lasers.
			# De theta is de verticale hoek tussen het het middelpunt en het snijpunt.
			# De phi is de horizontale hoek, oftewel hoe ver het platform op dat moment gedraaid is.
			for j in range(len(data_array)):
				radius = math.sqrt(float(data_array[j][1]/sinus_hoek)**2+float(data_array[j][0])**2)
				theta = np.arctan(float(data_array[j][0])/float(data_array[j][1]))
				# RadiusThetaPhi.append([radius, theta, phi])

			# Hierna worden de bolcoördinaten omgezet naar XYZ-coördinaten
				xVal = radius * np.sin(theta) * np.cos(phi)
				yVal = radius * np.sin(theta) * np.sin(phi)
				zVal = radius * np.cos(theta)
				XYZ.append([xVal, yVal, zVal])


		# for i in range(len(RadiusThetaPhi)):
		#	radius = RadiusThetaPhi[i][0]
		#	theta = RadiusThetaPhi[i][1]
		#	phi = RadiusThetaPhi[i][2]
		#	xVal = radius * np.sin(theta) * np.cos(phi)
		#	yVal = radius * np.sin(theta) * np.sin(phi)
		#	zVal = radius * np.cos(theta)
		#	XYZ.append([xVal, yVal, zVal])
		
		ConverteerNaarPly(XYZ)
