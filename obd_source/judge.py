from DataStore import CDataStore
import setting

class SumScore:
    @staticmethod   
    def calculData():
        CDataStore.ScoreSum=0
            #        for dt in CDataStore.ScoreData:
            #CDataStore.ScoreSum += CDataStore.ScoreData[dt]
            
            
            if CDataStore.ScoreData['speed'] == -1: #can read OBD data
                # warning to user & deactive keyboard
                CDataStore.Level = -1
            
            elif CDataStore.forceSteering != -1 || CDataStore.forceSpeed != -1 CDataStore.forceWeather != -1:
                CDataStore.Level = 3
            
            else:
                for item, value in CDataStore.ScoreData.iteritems(): #certificate key value, value in ScoreData Dict
                    if value == -1:
                        if item == 'rain' || item == 'snow':
                            #warning that system can't get weather data
                    else:
                        if item == 'speed':
                            CDataStore.ScoreSum += value*speedWeightedVal
                        elif item == 'rain' || item == 'snow':
                            CDataStore.ScoreData += value*weahterWeightedVal
                        elif item == 'steering':
                            CDataStore.ScoreData += value*steeringWeightedVal
                        else:
                            CDataStore.ScoreData += value


    @staticmethod
    def jugement():
        if  setting.SafetyStand['stand0'] <= CDataStore.ScoreSum < setting.SafetyStand['stand1']:
            CDataStore.Level = 1
        elif setting.SafetyStand['stand1'] <= CDataStore.ScoreSum < setting.SafetyStand['stand2']:
            CDataStore.Level = 2
        elif setting.SafetyStand['stand2'] <= CDataStore.ScoreSum:
            CDataStore.Level = 3
        else:
            return -1
        return 0

    def resetSumScore():
        CDataStore.ScoreSum = 0

