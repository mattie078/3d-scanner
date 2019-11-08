import numpy as np

# deze functie maakt een ply bestand van drie lists met punten.

def CalculateXYZ(self):

	X1=[]
	Y1=[]
	Z1=[]
	
	for i in range(0,73): 
		
		path = '..\\sphereCoords\\list' + str(i) + '.txt'
		data_array = np.loadtxt(fname=path)

		for j in range(0, data_array.shape[0]):
			X1.append(data_array[j][0] * np.sin(data_array[j][1]) * np.cos(data_array[j][2])) 
			Y1.append(data_array[j][0] * np.sin(data_array[j][1]) * np.sin(data_array[j][2])) 
			Z1.append(data_array[j][0] * np.cos(data_array[j][1])) 
	
	convertToPly(X1,Y1,Z1)


def convertToPly(x, y, z):
	# er wordt een bestand aangemaakt om de gegevens in op te slaan
	file = open("pointCloud.ply", "w+")

	# de  header van het bestand wordt aangemaakt.
	header = []
	for i in range(9):
		header.append("0")
	header[0] = "ply"
	header[1] = "format ascii 1.0"
	header[2] = "element vertex " + str(len(x))
	header[3] = "property float32 x"
	header[4] = "property float32 y"
	header[5] = "property float32 z"
	header[6] = "element face 0"
	header[7] = "property list uint8 int32 vertex_indices"
	header[8] = "end_header"

	# de header wordt toegevoegd aan het bestand
	for i in range(len(header)):
		file.write(header[i]+"\n")

	# coördinaten worden toegevoegd aan het bestand
	for i in range(len(x)):
		file.write(str(x[i])+" ")
		file.write(str(y[i])+" ")
		file.write(str(z[i])+"\n")
	file.close()

CalculateXYZ(0)