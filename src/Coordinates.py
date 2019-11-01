import cv2
import numpy as np
import pandas as pd


class Coordinates:

    def calculateCoordinates(self):
        for i in range(73):
            # Pakt de fotos die net zijn gemaakt
            path = "../FotosHSV/filter" + str(i) + ".jpg"
            new_image = cv2.imread(path)

            # Kijkt en slaat de pixels op in xycoordinates die wit zijn 
            indices = np.where(new_image == [255])

            coordinates = list(zip(indices[0], indices[1]))
            coordinatesNoDupes = []

            for index in coordinates:
                if index not in coordinatesNoDupes:
                    coordinatesNoDupes.append(index)
            zipped_list = coordinatesNoDupes[:]

            df = pd.DataFrame(zipped_list, columns={'yVal', 'xVal'})
            avgList = np.zeros((df['yVal'].nunique(), 2), dtype=np.int64)
            listWalker = 0
            for j in range(0,1080):
                temp = df[df.yVal == j]
                if not temp.empty:
                    avg = temp['xVal'].max() - temp['xVal'].min()
                    avgList[listWalker] = [j, avg]
                    listWalker += 1
            print("Finished calc:"+str(i))
            np.savetxt('..\calcs\\tempCalc' + str(i) + '.txt', avgList, fmt='%d')

    calculateCoordinates(0)