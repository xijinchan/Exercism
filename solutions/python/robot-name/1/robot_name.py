import random

class Robot:

    name = None
    
    def __init__(self):
        self.reset()

    def reset(self):
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        random.seed()
        
        self.name = alphabet[random.randint(0,25)] + alphabet[random.randint(0,26)] + str(random.randint(100,999))