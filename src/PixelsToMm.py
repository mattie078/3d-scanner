import cv2
import numpy as np
import pandas as pd


class PixelsToMm:

    def calculate_real_distances(self):
        # Formula from calibration: 
        # pixels = (6,3933* mm) - 10,338

        # pixels = a*milimeters + b
        a = 6.3933
        b = -10.338
        hoek = 12
        platform_pixel_y_waarde = 800

        # Wat is dit? @Herman
            # Dit is het aantal pixels dat de foto hoog is. Full HD foto, dus 1920 x 1080.
            # Wordt gebruikt bij de hoogte berekening.
        verticale_resolutie = 1080

        sinus_hoek = np.sin(np.deg2rad(hoek))
        for i in range(73):
            # Pakt de lijnbreedtes per y-coordinaat die net zijn berekend
            path = '..\\calcs\\tempCalc'+str(i)+'.txt'
            data_array = np.loadtxt(fname=path, dtype='int')

            # Meer comments pls
            
            end_array = np.zeros((data_array.shape[0], 3))
            for j in range(0, data_array.shape[0]):
                y_waarde = data_array[j][0]
                pixel_hoogte = verticale_resolutie - (y_waarde - platform_pixel_y_waarde)
                pixel_breedte = data_array[j][1]

                mm_hoogte = ((pixel_hoogte - b) / a)
                mm_breedte = ((pixel_breedte - b) / a)
                mm_afstand = mm_breedte/sinus_hoek
                r = np.square(mm_hoogte)+np.square(mm_afstand)
                tau = np.rad2deg(np.arctan(mm_hoogte/mm_afstand))
                phi = hoek + i * (360/73)
                end_array[j] = [r, tau, phi]
            print("Finished sphereCoords:"+str(i))
            np.savetxt('..\\sphereCoords\\list' + str(i) + '.txt', end_array, fmt='%f')

    calculate_real_distances(0)
