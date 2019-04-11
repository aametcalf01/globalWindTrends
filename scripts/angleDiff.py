import math
import numpy as np
def calcAngleDiff(a1,a2):
    a1 = math.radians(a1)
    a2 = math.radians(a2)
    
    return abs(math.degrees(math.atan2(math.sin(a2-a1), math.cos(a2-a1))))

