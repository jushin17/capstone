import analysis

class SumScore:
    scoreSum = 0
    level = 1

    @staticmethod   
    def calculData():
        SumScore.scoreSum=0
        for dt in analysis.DataScore.score:
            SumScore.scoreSum += analysis.DataScore.score[dt]

    @staticmethod
    def jugement():
        if 0 <= SumScore.scoreSum <= 59:
            SumScore.level = 1
        elif 60 <= SumScore.scoreSum <= 79:
            SumScore.level = 2
        elif 79 <= SumScore.scoreSum:
            SumScore.level = 3
        else:
            return -1
        return 0

