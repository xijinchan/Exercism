class CustomSet:
    def __init__(self, elements=[]):
        self.elements = [k for k in elements]

    def isempty(self):
        return bool(self.elements == [])

    def __contains__(self, element):
        return bool(element in self.elements)

    def issubset(self, other):
        if self.elements == []:
            return True

        return bool(all(k if k in other.elements else False for k in self.elements))

    def isdisjoint(self, other):
        return bool(not([k for k in self.elements if k in other.elements]))

    def __eq__(self, other):
        if len(self.elements) != len(other.elements): return False
        return all(k in other.elements for k in self.elements)
    
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        common = [k for k in self.elements if k in other.elements]
        return CustomSet(common)

    def __sub__(self, other):
        dif = [k for k in self.elements if k not in other.elements]      
        return CustomSet(dif)

    def __add__(self, other):
        unique = set(self.elements + other.elements)   
        return CustomSet(unique)
