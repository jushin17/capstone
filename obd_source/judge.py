from DataStore import CDataStore

class SumScore:
    @staticmethod   
    def calculData():
        CDataStore.ScoreSum=0
        for dt in CDataStore.ScoreData:
            CDataStore.ScoreSum += CDataStore.ScoreData[dt]

    @staticmethod
    def jugement():
        if 0 <= CDataStore.ScoreSum <= 59:
            CDataStore.Level = 1
        elif 60 <= CDataStore.ScoreSum <= 79:
            CDataStore.Level = 2
        elif 79 <= CDataStore.ScoreSum:
            CDataStore.Level = 3
        else:
            return -1
        return 0

