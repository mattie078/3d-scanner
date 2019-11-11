import numpy as np

def ConvertToPly(x, y, z):
	# A file will be made to store the pointcloud
	file = open("pointCloud.ply", "w+")

	# Store the standard header in an array
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

	# Adds the header to the file
	for i in range(len(header)):
		file.write(header[i]+"\n")

	# Adds the coordinates to the Pointcloud file
	for i in range(len(x)):
		file.write(str(x[i])+" ")
		file.write(str(y[i])+" ")
		file.write(str(z[i])+"\n")
	file.close()
	print("Pointcloud has been made!")
