import analysis

class SumScore:
    scoreSum = 0
    level = 1

    @staticmethod   
    def calculData():
        self.scoreSum=0
        for dt in analysis.DataScore.score
            self.scoreSum += analysis.DataScore.score[dt]

    @staticmethod
    def jugement(self):
        if 0 <= self.scoreSum <= 59:
            SumScore.level = 1
        elif 60 <= self.scoreSum <= 79:
            SumScore.level = 2
        elif 79 <= self.scoreSum:
            SumScore.level = 3
        else:
            return -1
        return 0

