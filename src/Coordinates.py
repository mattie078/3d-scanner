import cv2
import numpy as np
import pandas as pd
import time


class Coordinates:

    def calculate_coordinates(self):
        platform_pixel_y_waarde = 570
        for i in range(73):
            # Pakt de fotos die net zijn gemaakt
            path = "..\\FotosHSV\\filter" + str(i) + ".jpg"
            new_image = cv2.imread(path)

            # Pakt alle coordinaten waarop de foto de punten wit zijn
            indices = np.where(new_image == [255])

            # Pakt alle coordinaten en zet ze in een list
            coordinates = list(zip(indices[0], indices[1]))

            # Pakt alle coordinates en verwijderd alle duplicates
            coordinates_no_dupes = []
            for index in coordinates:
                if index not in coordinates_no_dupes:
                    coordinates_no_dupes.append(index)
            zipped_list = coordinates_no_dupes[:]

            df = pd.DataFrame(zipped_list, columns={'yVal', 'xVal'})

            # Prepares iterator to be the amount of unique Y values to optimize runtime 
            df2 = df["yVal"]
            df2 = df2.drop_duplicates()
            # negeert y-waardes onder het platform
            df2 = df2[(df2 < platform_pixel_y_waarde)]
            
            # This code gets all Y values from specific X value (X values are still in array type)
            avg_list = []

            for index_old, non_duplicated_yVal in df2.iteritems():
                val = df.loc[df["yVal"] == non_duplicated_yVal, "xVal"]

                # val.real returns array with values instead of an dataframe
                val_np = np.array(val.real)
                if val_np.size != 0:
                    # alleen waardes aan de linkerkant van de laser in het midden moeten meegenomen worden.
                    # Als een x-waarde hoger is dan die van de middenlijn betekent dit dat de laser op deze y-waarde
                    # achter het middelpunt van het draaivlak schijnt en er dus geen voorwerp tussen staat op die
                    # hoogte, oftewel: het voorwerp bevindt zich onder deze y-waarde en deze punten moeten dus
                    # genegeerd worden. (zie Documenten/xyCalcsAfbeelding1.png)
                    if val_np.max(axis=0) < 1120:  # opgemeten uit foto's. kan accurater als de laser recht hangt.
                        length = val_np.max(axis=0)-val_np.min(axis=0)
                        avg_list.append([non_duplicated_yVal, length])

            print("Finished calc:"+str(i))
            np.savetxt('..\\calcs\\tempCalc' + str(i) + '.txt', avg_list, fmt='%d')

    calculate_coordinates(0)