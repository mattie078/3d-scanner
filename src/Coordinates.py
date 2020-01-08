import cv2
import numpy as np
import pandas as pd
from PixelsToMm import PixelsToMm
import os


class Coordinates:

    def calculate_coordinates(self, i):
        # De de afstand tussen de bovenkant van de foto en de voorkant van het platform (in pixels)
        # platform_pixel_y_waarde = 570 NIET MEER NODIG
        # Pakt de fotos die net zijn gemaakt
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        path = dir_path + "/../FotosHSV/filter" + str(i) + ".jpg"
        new_image = cv2.imread(path)

        # Pakt alle coordinaten waarop de foto de punten wit zijn
        indices = np.where(new_image == [255])

        # Pakt alle coordinaten en zet ze in een list
        coordinates = list(zip(indices[0], indices[1]))
        # coordinates2 = list(zip(indices2[0], indices2[1]))

        # Pakt alle coordinates en verwijderd alle duplicates
        coordinates_no_dupes1 = []
        # coordinates_no_dupes = []

        setA = set(map(tuple, coordinates))
        setB = set(map(tuple, coordinates_no_dupes1))

        for o in setA:
            if o not in setB:
                coordinates_no_dupes1.append(o)

        # Loop
        # for index in coordinates:
        #     if index not in coordinates_no_dupes:
        #         coordinates_no_dupes.append(index)

        zipped_list = coordinates_no_dupes1[:]
        df = pd.DataFrame(zipped_list, columns={'yVal', 'xVal'})

        # Haalt alle unieke Y waardes uit de dataframe en slaat ze op in een nieuwe
        df2 = df["yVal"]
        df2 = df2.drop_duplicates()
        # negeert y-waardes onder het platform
        # df2 = df2[(df2 < platform_pixel_y_waarde)]    NIET MEER NODIG

        # Deze loop haalt alle X waardes uit de dataframe die bij een bepaalde Y waarde hoort (X type = dataframe)
        avg_list = []

        for index_old, non_duplicated_yVal in df2.iteritems():
            val = df.loc[df["yVal"] == non_duplicated_yVal, "xVal"]

            # val.real returned 'normale' array inplaats van een dataframe (voor makkelijkere verwerking)
            val_np = val.to_numpy().real
            if val_np.size != 0:
                # alleen waardes aan de linkerkant van de laser in het midden moeten meegenomen worden.
                # Als een x-waarde hoger is dan die van de middenlijn betekent dit dat de laser op deze y-waarde
                # achter het middelpunt van het draaivlak schijnt en er dus geen voorwerp tussen staat op die
                # hoogte, oftewel: het voorwerp bevindt zich onder deze y-waarde en deze punten moeten dus
                # genegeerd worden. (zie Documenten/xyCalcsAfbeelding1.png)
                # X-waarde van de rechter laser. Opgemeten uit foto's.
                if val_np.max(axis=0) < 1120:
                    length = val_np.max(axis=0)-val_np.min(axis=0)
                    avg_list.append([non_duplicated_yVal, length])

        # print("Finished calc:"+str(i))  # NIET MEER NODIG
        # np.savetxt('..\\temps\\calcs\\tempCalc' + str(i) + '.txt', avg_list, fmt='%d')
        PixelsToMm.calculate_real_distances(0, i, avg_list)   # linkt nu direct door.
        # Bespaart tijd omdat we nu niet meer naar de harde schijf lezen/schrijven, alles blijft in RAM.

co = Coordinates()
co.calculate_coordinates(1)