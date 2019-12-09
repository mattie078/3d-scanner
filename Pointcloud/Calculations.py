import numpy as np
import math as math
class Calculations:
    angle = 12

    def calculateHypothenuse(self):
        for x in range(73):
            path = '..\\temps\\xycoordinates\\tempXY' + str(x) + '.txt'
            getmm_array = np.loadtxt(fname=path, dtype='float')
            # print(getmm_array)

            for y in range(0,getmm_array.shape[0]):
                
                getmm_array[y][0]=getmm_array[y][0]/math.sin(12*(math.pi/180))
                # print(getmm_array[y][0])
                variabel + int(y) = getmm_array[y][0]
                print(variabel +int(y))

calc = Calculations()
calc.calculateHypothenuse()




