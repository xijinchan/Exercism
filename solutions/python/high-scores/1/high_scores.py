class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        print(self.scores)
        return self.scores[-1:][0]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        top_three = []
        scores_shortlist = [k for k in self.scores]

        for _ in range(3):
            top_three.append(max(scores_shortlist))
            scores_shortlist.remove(max(scores_shortlist))
            if scores_shortlist == []: break

        return top_three
            
            