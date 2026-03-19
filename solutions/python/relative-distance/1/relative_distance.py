from collections import deque

class RelativeDistance:
    def __init__(self, family_tree):
        self.family_tree = family_tree
        print('init')
        

    def degree_of_separation(self, person_a, person_b):
        print('degree')
        visited = set()

        # check if person_a in dict
        person_a_found = False
        if person_a not in self.family_tree:
            for person in self.family_tree:
                if person_a in self.family_tree[person]:
                    person_a_found = True
                    if person_b in self.family_tree[person]: # if siblings
                        return 1
            if person_a_found == False:
                raise ValueError("Person A not in family tree.")
            
        # check if person_b in dict
        person_b_found = False
        if person_b not in self.family_tree:
            for person in self.family_tree:
                if person_b in self.family_tree[person]:
                    person_b_found = True
            if person_b_found == False:
                raise ValueError("Person B not in family tree.")
            
        queue = deque([(person_a, 0)])
        max_iterations = 1000
        i = 0

        while queue and i < max_iterations:
            person_tuple = queue.popleft() 
            person, degree = person_tuple
            
            # search children
            if person is person_b:
                return degree
            else:
                if person in self.family_tree:
                    for child in self.family_tree[person]:
                        if child not in visited and (child, degree + 1) not in queue:
                            queue.append((child, degree + 1))

            # search parents
            for parent in self.family_tree:
                for child in self.family_tree[parent]:
                    if child is person:
                        if parent is person_b:
                            return degree
                        if parent not in visited and (parent, degree + 1) not in queue:
                            queue.append((parent, degree + 1))
                        for child in self.family_tree[parent]:
                            if child is person_b:
                                return degree
                            if child not in visited and (child, degree) not in queue:
                                queue.append((child, degree + 1))
            if person not in visited:
                visited.add(person)
        i += 1

        raise ValueError("No connection between person A and person B.")