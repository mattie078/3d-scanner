import cv2
import numpy as np

class Coordinates():
    
    def calculateCoordinates():
        for i in range(73):
            # Pakt de fotos die net zijn gemaakt
            path = "Fotos/filter" + str(i) + ".jpg"
            new_image = cv2.imread(path)

            # Kijkt en slaat de pixels op in xycoordinates die wit zijn 
            indices = np.where(new_image == [255])

            coordinates = list(zip(indices[0], indices[1]))
            coordinatesNoDupes = []

            for index in coordinates:
                if index not in coordinatesNoDupes:
                    coordinatesNoDupes.append(index)

            zipped_list = coordinatesNoDupes[:]
            np.savetxt('xycoordinates.txt', zipped_list, fmt = '%d')