from .person import Person

class Instructor(Person):
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def add_exercise(self, student, exercise):
        student.exercises.append(exercise)

    def show_details(self):
      instructor = self.__dict__
      for prop, value in instructor.items():
        print(f'{prop}:\n{value}\n')
