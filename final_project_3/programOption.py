TESTMODE = 0
EXMODE = 1
mode = 0

class CSetting:
    SpeedStand=[0,80,100]
    
    #weighted value seted by admin.
    weatherWeightedVal = 1
    speedWeightedVal = 1
    steeringWeightedVal = 1

def StartSetMode(setMode):
    mode = setMode
    
