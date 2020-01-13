import numpy as np

def ConverteerNaarPly(xyz):
	# Een bestand wordt gemaakt om de pointCloud in op te slaan
	file = open("../temps/pointCloud.ply", "w+")

	# Pointclouds hebben een standaard header (http://people.math.sc.edu/Burkardt/data/ply/ply.txt)
	header = []
	for i in range(9):
		header.append("0")
	header[0] = "ply"
	header[1] = "format ascii 1.0"
	header[2] = "element vertex " + str(len(xyz))
	header[3] = "property float32 x"
	header[4] = "property float32 y"
	header[5] = "property float32 z"
	header[6] = "element face 0"
	header[7] = "property list uint8 int32 vertex_indices"
	header[8] = "end_header"

	# Voegt de header toe aan het bestand
	for i in range(len(header)):
		file.write(header[i]+"\n")

	# Voegt de coordinaten toe aan het bestand
	for i in range(len(xyz)):
		file.write(str(xyz[i][0])+" ")
		file.write(str(xyz[i][1])+" ")
		file.write(str(xyz[i][2])+"\n")
	file.close()
	print("Pointcloud has been made!")
