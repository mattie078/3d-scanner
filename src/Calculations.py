import numpy as np
import math as math
from ConverteerNaarPly import ConverteerNaarPly as ConverteerNaarPly
class Calculations:
    angle = 12
    rotations = 73

    def calculateHypothenuse(self, x):
        path = '..\\temps\\xycoordinates\\tempXY' + str(x) + '.txt'
        getmm_array = np.loadtxt(fname=path, dtype='float')

        for y in range(0,getmm_array.shape[0]):                
            getmm_array[y][0]=getmm_array[y][0]/math.sin(np.deg2rad(12))  #12 veranderen naar angle


        return getmm_array

    def cartesianToSpherical(self, hypo_array, x):
        polarangle = (.5*math.pi)-math.atan(hypo_array[y][1]/hypo_array[y][0]) #90-angle of angle
        radius = math.sqrt(hypo_array[y][1]**2 + hypo_array[y][0]**2)
        motorAngle = (360/73*x) # checken voor draaifoto volgorde
        return polarangle,radius,motorAngle

    def SphericalToCartesian(self, polarangle, radius, motorAngle):
        xcoordinate = radius*math.sin(polarangle)*math.cos(motorAngle)
        ycoordinate = radius*math.sin(polarangle)*math.sin(motorAngle)
        zcoordinate = radius*math.cos(polarangle)
        return xcoordinate,ycoordinate,zcoordinate

calc = Calculations()
# convertply = ConverteerNaarPly()
xyzArray = []
for x in range(73): #73 later nog veranderen in rotations
    hypo_array = calc.calculateHypothenuse(x)
    for y in range(0,hypo_array.shape[0]):
        polarangle, radius, motorAngle = calc.cartesianToSpherical(hypo_array, x)
        xcoordinate, ycoordinate, zcoordinate = calc.SphericalToCartesian(polarangle, radius, motorAngle)
        xyzArray.append([xcoordinate, ycoordinate, zcoordinate])
# print(xyzArray)        
ConverteerNaarPly(xyzArray)

    # print(hypo_array)
