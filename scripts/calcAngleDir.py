import math
import numpy as np
def calcAngleDir(dirList, spdList):
    """This function takes a list of direction and speed observations
    and calculates the average wind direction"""
    if len(dirList)!=len(spdList):
        return "Direction and speed lists must be the same lenght"
    else:
        #U is considered to be the east west direction
        #V is considered to be the south north direction
        U = []
        V = []
        
        for i in range(len(dirList)):
            direction = dirList[i]
            speed = spdList[i]

            u = speed * math.sin(2*math.pi*direction/360)
            #print("u = ",u)
            v = speed * math.cos(2*math.pi*direction/360)
            #print("v = ",v)
            U.append(u)
            V.append(v)
        mean_U = np.mean(U)
        mean_V = np.mean(V)
        #print("mean U = ", mean_U)
        #print("mean V = ", mean_V)
        return compToAngle(mean_U, mean_V)

def compToAngle(u,v):
    """This function takes as argument component
    vectors u (E-W wind direction) and v (N-S wind direction)
    and outputs the vector angle in degrees"""
    rad = math.atan2(u,v)
    deg = math.degrees(rad)
    if deg<0:
        deg +=360
    return deg