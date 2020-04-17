from .person import Person
# import json


class Student(Person):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercises = list()

    def show_details(self):
        student = self.__dict__
        for prop, value in student.items():
            print(f'{prop}:\n{value}\n')


    # def print_details(self):
    #     new_dict = self.__dict__
    #     new_list = list()
    #     for exercise in new_dict["exercises"]:
    #         ex_dict = exercise.__dict__
    #         new_list.append(ex_dict)
    #     new_dict["exercises_list"] = new_list
    #     print(json.dumps(new_dict, indent=2))
