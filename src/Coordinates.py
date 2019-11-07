import cv2
import numpy as np
import pandas as pd
import time


class Coordinates:

    def calculateCoordinates(self):
        for i in range(73):
            # Pakt de fotos die net zijn gemaakt
            path = "../FotosHSV/filter" + str(i) + ".jpg"
            new_image = cv2.imread(path)

            # Kijkt en slaat de pixels op in xycoordinates die wit zijn 
            indices = np.where(new_image == [255])

            # for width in range(0,1920):
            #     for height in range(0,1080):
            #         print(indices[width][height])

            coordinates = list(zip(indices[0], indices[1]))
            coordinatesNoDupes = []

            for index in coordinates:
                if index not in coordinatesNoDupes:
                    coordinatesNoDupes.append(index)
            zipped_list = coordinatesNoDupes[:]

            df = pd.DataFrame(zipped_list, columns={'yVal', 'xVal'})

            # Prepares iterator to be the amount of unique Y values to optimize runtime 
            df2 = df["yVal"]
            df2 = df2.drop_duplicates()
            
            # This code gets all Y values from specific X value (X values are still in array type)
            listWalker = 0
            avgList = []

            for index_old, non_dublicated_yVal in df2.iteritems(): 
                val = df.loc[df["xVal"] == non_dublicated_yVal, "yVal"]

                # val.real returns array with values instead of an dataframe
                val_np = np.array(val.real)
                if val_np.size != 0:

                    length = val_np.max(axis=0)-val_np.min(axis=0)
                    avgList.append([non_dublicated_yVal, length])

            print("Finished calc:"+str(i))
            np.savetxt('..\calcs\\tempCalc' + str(i) + '.txt', avgList, fmt='%d')

    calculateCoordinates(0)