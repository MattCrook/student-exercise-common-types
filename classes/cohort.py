class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()


    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def show_details(self):
      cohort = self.__dict__
      for prop, value in cohort.items():
        print(f'{prop}:\n{value}\n')
