class CDataStore:
    SensorData = {}
    ScoreData = {}
    ScoreSum = 0
    Level = 1
    
    #weighted value seted by admin.
    weatherWeightedVal = 1
    speedWeightedVal = 1
    steeringWeightedVal = 1
    
    
    def isRoadData():
        if ScoreData['speed'] == -1:
            return false
        else:
            return true

    @staticmethod
    def isChanged():
        return True
    
    
