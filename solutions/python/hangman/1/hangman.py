# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.revealed = []

    def guess(self, char):
        if self.get_status() == STATUS_LOSE: 
            raise ValueError("The game has already ended.")
        if self.get_status() == STATUS_WIN:
            raise ValueError("The game has already ended.")            
        if char in self.word:
            if char in self.revealed:
                self.remaining_guesses -= 1
            else:
                self.revealed.append(char)
        else:
            self.remaining_guesses -= 1

    def get_masked_word(self):
        masked = ''.join([k if k in self.revealed else '_' for k in self.word])
        return masked

    def get_status(self):
        if all([k if k in self.revealed else False for k in self.word]):
            return STATUS_WIN
        elif self.remaining_guesses < 0:
            return STATUS_LOSE
        else:
            return STATUS_ONGOING
