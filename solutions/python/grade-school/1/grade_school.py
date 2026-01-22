class School:
    def __init__(self):
        self.roster_full = {}
        self.add_successful = []

    def add_student(self, name, grade):
        try:
            all_names = [k for j in list(self.roster_full.values()) for k in j]
            if name not in all_names:
                names = self.roster_full[grade]
                names.append(name)
                names.sort()
                self.roster_full.update({grade: names})
                self.add_successful.append(True)
            else:
                self.add_successful.append(False)
        except:
            self.roster_full.update({grade: [name]})
            self.add_successful.append(True)
        self.roster_full = dict(sorted(self.roster_full.items()))

    def roster(self):
        if self.roster_full == {}:
            return []
        else:
            output = [k for j in list(self.roster_full.values()) for k in j]
            return output

    def grade(self, grade_number):
        try:
            output = self.roster_full[grade_number]
        except:
            output = []
        return output

    def added(self):
        return self.add_successful
