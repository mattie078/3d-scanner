import numpy as np
import math as math
class Calculations:
    angle = 12
    rotations = 73

    def calculateHypothenuse(self, x):
        path = '..\\temps\\xycoordinates\\tempXY' + str(x) + '.txt'
        getmm_array = np.loadtxt(fname=path, dtype='float')

        for y in range(0,getmm_array.shape[0]):                
            getmm_array[y][0]=getmm_array[y][0]/math.sin(12*(math.pi/180))  #12 veranderen naar angle

        return getmm_array

    def cartesianToSpherical(self, hypo_array, x):
        polarangle = math.atan(hypo_array[y][1]/hypo_array[y][0])/(math.pi/180) #90-angle of angle
        radius = math.sqrt(math.pow(hypo_array[y][1], 2) + math.pow(hypo_array[y][0], 2))
        motorAngle = (360/73*x) # checken voor draaifoto volgorde
        return polarangle,radius,motorAngle

    def SphericalToCartesian(self, polarangle, radius, motorAngle):
        xcoordinate = radius*math.sin(90-polarangle)*math.cos(motorAngle)
        ycoordinate = radius*math.cos(90-polarangle)*math.sin(motorAngle)
        zcoordinate = radius*math.cos(90-polarangle)
        return xcoordinate,ycoordinate,zcoordinate

calc = Calculations()

for x in range(73): #73 later nog veranderen in rotations
    hypo_array = calc.calculateHypothenuse(x)
    for y in range(0,hypo_array.shape[0]):
        polarangle, radius, motorAngle = calc.cartesianToSpherical(hypo_array, x)
        xcoordinate, ycoordinate, zcoordinate = calc.SphericalToCartesian(polarangle, radius, motorAngle)
    # print(hypo_array)




