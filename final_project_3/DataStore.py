class CDataStore:
    SensorData = {}
    ScoreData = {}
    ScoreSum = 0
    Level = 1
    
    StateSpeed = False
    StateSteering = False
    StateGear = False
    StateRain = False
    StateRoad = False

    StateSpeedValue = -1
    StateSteeringValue = -1
    StateGearValue = -1
    StateRainValue = -1
    StateRoadValue = -1
    
    #weighted value seted by admin.
    weatherWeightedVal = 1
    speedWeightedVal = 1
    steeringWeightedVal = 1

    forceSteering = -1
    forceSpeed = -1
    forceWeather = -1
    
    SpeedStand=[0,80,100]
    
    @staticmethod
    def isChanged():
        return True
     

    
