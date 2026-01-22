import itertools
import math

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(item in self.lst)

    @property
    def lst(self):
        print(self.score)
        allergies_list = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats'
        }

        # find summands of score
        allergies_shortlist = [k for k in allergies_list if k <= self.score]
        allergies_numbers = None
        done = False
        if self.score > 255: self.score = self.score - 2 ** int(math.log(self.score,2)) 
            
        for i in range(len(allergies_shortlist)+1):
            permutations = list(itertools.permutations(allergies_shortlist, i))
            for k in permutations:
                if sum(k) == self.score:
                    allergies_numbers = k
                    done = True
                    break
            if done == True: break

        output = [allergies_list[k] for k in allergies_numbers]
        return output