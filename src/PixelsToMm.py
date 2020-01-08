import cv2
import numpy as np
import pandas as pd


class PixelsToMm:

    def calculate_real_distances(self, i, tempList):
        # Formule van de kalibratie: 
        # pixels = (6,3933* mm) - 10,338

        # pixels = a*milimeters + b
        a = 6.3933
        b = -10.338
        hoek = 12
        # platform_pixel_y_waarde = 570 # opgemeten uit de verschillende foto's die we genomen hebben. Zat marge op.
                                        # NIET MEER NODIG
        # Pakt de lijnbreedtes per y-coordinaat die net zijn berekend
        data_array = np.array(tempList, dtype='int')

        end_array = []
        # De actuele milimeters voor elke waarde in tempCalc berekenen
        for j in range(0, data_array.shape[0]):
            y_waarde = data_array[j][0]
            # pixel_hoogte ging eerst fout, dit is hoe het zou moeten. (zie xyCalcsAfbeelding2.png)
            pixel_hoogte = y_waarde
            pixel_breedte = data_array[j][1]

            if pixel_breedte < 250: # groot schepnet tegen ruis

                mm_hoogte = ((pixel_hoogte - b) / a)
                mm_breedte = ((pixel_breedte - b) / a)

                end_array.append([mm_breedte, mm_hoogte])

        print("Finished xycoordinates:"+str(i))
        np.savetxt('..\\temps\\xycoordinates\\tempXY' + str(i) + '.txt', end_array, fmt='%f')