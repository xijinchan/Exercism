class Garden:
    students_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    
    def __init__(self, diagram, students = students_list):
        self.diagram = [diagram.split('\n')[k:k+1][0] for k in range(len(diagram.split('\n')))]
        self.students = students
        self.students.sort()

    def plants(self, student):
        plants_list = {
            'C': 'Clover',
            'G': 'Grass',
            'R': 'Radishes',
            'V': 'Violets'
        }
        
        p = self.diagram[0][2 * self.students.index(student):2 * self.students.index(student) + 2] + self.diagram[1][2 * self.students.index(student):2 * self.students.index(student) + 2]

        return [plants_list[k] for k in p]