class BowlingGame:
    def __init__(self):
        self.score_ = 0
        self.frame_score = 0
        self.frame = 0.0
        self.scores = []
        self.spare = False

    def roll(self, pins):
        if pins < 0 or pins > 10: raise ValueError(f'game.roll({pins})')
        if len(self.scores) > 20: raise ValueError(f'game.roll({pins})')
        if all([len(self.scores) == 20, 10 not in self.scores[-2:], sum(self.scores[-2:]) != 10]): raise ValueError(f'game.roll({pins})')
        
        self.scores.append(pins)

        if len(self.scores) > 2 and self.frame < 10.0:
            if self.scores[-3] == 10: # bonus for strike
                self.score_ += sum(self.scores[-2:])
            if self.spare == True: # bonus for spare
                self.score_ += sum(self.scores[-1:])
                self.spare = False
        
        if pins == 10: # score strike
            self.score_ += 10
            self.frame += 1.0
            if self.frame == 11.0 and sum(self.scores[-3:]) == 30:
                self.score_ += sum(self.scores[-3:-1])
            if self.frame >= 11.0:
                if all([self.scores[-3] == 10, self.scores[-2] is not 10, self.scores[-1] == 10]): raise ValueError(f'game.roll({pins})')
        elif self.frame < 10.0: # score spares
            self.frame_score += pins
            self.frame += 0.5
            if self.frame % 1 == 0:
                if sum(self.scores[-2:]) > 10: raise ValueError(f'game.roll({pins})')
                if self.scores[-1] < 10 and sum(self.scores[-2:]) == 10:
                    self.spare = True
                self.score_ += self.frame_score
                self.frame_score = 0
        else: # after frame 10.0
            self.frame += 0.5
            self.score_ += pins
            if self.frame == 11.0 and self.scores[-4] == 10:
                self.score_ += sum(self.scores[-3:-2])
            if self.frame == 11.0 and sum(self.scores[-2:]) > 10: raise ValueError(f'game.roll({pins})')

    def score(self):
        if self.scores == []: raise ValueError(f'game.score()')
        if self.frame < 10.0: raise ValueError(f'game.score()')
        if self.frame == 11.0 and self.scores[-2] == 10: raise ValueError(f'game.score()')
        if self.frame == 10.0 and sum(self.scores[-2:]) == 10: raise ValueError(f'game.score()')
            
        return self.score_