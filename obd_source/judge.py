import analysis



class SumScore(DataScore):
    self.scoreSum = 0
    SumScore.jugde = 1
    def calculData(self):
        self.scoreSum=0
        for dt in analysis.DataScore.score
            self.scoreSum += analysis.DataScore.score[dt]

    def jugement(self):
        if 0 <= self.scoreSum <= 59:
            SumScore.judge = 1
        elif 60 <= self.scoreSum <= 79:
            SumScore.judge = 2
        elif 79 <= self.scoreSum:
            SumScore.judge = 3
        else:
            return -1
        return 0

