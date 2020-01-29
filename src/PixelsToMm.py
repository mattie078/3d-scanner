import cv2
import numpy as np
import pandas as pd


class PixelsToMm:

    def calculate_real_distances(self, i, tempList):
        # Formule van de kalibratie: 
        # milimeters = 0.2 * (pixels - 5)
        # mm = a * (px - b)
        # nb: de b hier is de breedte van een laserstraal, omdat we de buitekant van de laserstralen meten. Ook op een afstand van 0 mm hebben we dus 5 pixels aan afstand.
        # Voor het berekenen van de hoogte in milimeters maakt de dikte van de laser niet uit; hier is de b in de formule dus gewoon 0.
        a = 0.2
        b = 5
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

                mm_hoogte = a*pixel_hoogte
                mm_breedte = a*(pixel_breedte-b)

                end_array.append([mm_breedte, mm_hoogte])

        print("Finished xycoordinates:"+str(i))
        np.savetxt('../temps/xycoordinates/tempXY' + str(i) + '.txt', end_array, fmt='%f')
