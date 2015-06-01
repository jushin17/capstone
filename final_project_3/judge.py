from DataStore import CDataStore
from programOption import CSetting
import audioplay

cnt = 0

oldlevelstate = 1

class SumScore(CSetting):
    @staticmethod   
    def calculData():
        CDataStore.ScoreSum=0
            #        for dt in CDataStore.ScoreData:
            #CDataStore.ScoreSum += CDataStore.ScoreData[dt]
            
	if CDataStore.ScoreData['speed'] == -1:
                # warning to user & deactive keyboard
                CDataStore.Level = -1
            
            #forceData is user input
	elif CDataStore.forceSteering != -1 or CDataStore.forceSpeed != -1 or CDataStore.forceWeather != -1:
                CDataStore.Level = 3
        
	else:
                for item, value in CDataStore.ScoreData.iteritems(): #certificate key value, value in ScoreData Dict
                    if value == -1:
			if item == 'rain' or item == 'snow':
				CDataStore.ScoreSum +=0
			elif item == 'speed':
				print CSetting.speedWeightedVal
				print value
				CDataStore.ScoreSum += 20*CSetting.speedWeightedVal
                    else:
                        if item == 'speed':
			    print CSetting.speedWeightedVal
			    print value
                            CDataStore.ScoreSum += value*CSetting.speedWeightedVal
                        elif item == 'rain' or item == 'snow':
			    print CSetting.weatherWeightedVal
			    print value

                            CDataStore.ScoreData += value*CSetting.weahterWeightedVal
			    
                        elif item == 'steering':
			    print CSetting.steeringWeightedVal
                            CDataStore.ScoreSum += value*CSetting.steeringWeightedVal
                        else:
                            CDataStore.ScoreSum += value

    @staticmethod
    def jugement():
        for k in CDataStore.SensorData:
            print k, ' : ', CDataStore.SensorData[k], ' ',
        print '\n'
        for p in CDataStore.ScoreData:
            print p, ' : ', CDataStore.ScoreData[p], ' ',
        print '\n'


        if 0 <= CDataStore.ScoreSum <= 59:
            CDataStore.Level = 1
        elif 60 <= CDataStore.ScoreSum <= 79:
            CDataStore.Level = 2
        elif 79 <= CDataStore.ScoreSum:
            CDataStore.Level = 3
        else:
            return -1
        return 0

