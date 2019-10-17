# deze functie maakt een ply bestand van drie lists met punten.

def ConvertToPly(x,y,z):
	# er wordt een bestand aangemaakt om de gegevens in op te slaan
	file = open("pointCloud.ply","w+")

	# de  header van het bestand wordt aangemaakt.
	header = []
	for i in range(9):
		header.append("0")
	header[0] = "ply"
	header[1] = "format ascii 1.0"
	header[2] = "element vertex "+ str(len(x))
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
		#print('X ' + str(x[i]))
		file.write(str(y[i])+" ")
		#print('Y ' + str(y[i]))
		file.write(str(z[i])+"\n")
		#print('Z ' + str(z[i]))

	file.close()
