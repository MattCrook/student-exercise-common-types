from classes import Cohort, Instructor, Student, Exercise

# Create instances of exercises
list_exercise = Exercise("Lists", "Python")
multiple_inheritance_exercise = Exercise("Multiple Inheritance", "Python")
interface_exercise = Exercise("Interfaces", "C#")
dictionaries_exercise = Exercise("Dictionaries", "Python")
function_currying = Exercise("Function Currying", "Javascript")
classes_exercise = Exercise("Classes", "Python")

#Create instances of cohorts
cohort_37 = Cohort("Cohort 37")
cohort_38 = Cohort("Cohort 38")
cohort_39 = Cohort("Cohort 39")

#Create Instances of instructors
instructor_andy = Instructor("Andy", "Collins", "andy@slack.com", cohort_38, "JavaScript")
instructor_jisie = Instructor("Jisie", "David", "jisie@slack.com", cohort_38, "Python")
instructor_steve = Instructor("Steve", "Brownlee", "steve@slack.com", cohort_37, "JavaScript")

#Create instances of students
student_matt = Student("Matt", "Crook", "matt@slack.com", cohort_38)
student_mike = Student("Mike", "Pence", "vp@slack.com", cohort_38)
student_kub = Student("Kub", "Docker", "k8@slack.com", cohort_38)
student_sara = Student("Sara", "Vue", "svue@slack.com", cohort_37)
student_bruce = Student("Bruce", "Brown", "bruce@slack.com", cohort_39)

# Have the instructors assign an exercise to a student
instructor_andy.add_exercise(student_matt, list_exercise)
instructor_jisie.add_exercise(student_bruce, interface_exercise)
instructor_steve.add_exercise(student_kub, function_currying)
instructor_andy.add_exercise(student_mike, multiple_inheritance_exercise)
instructor_jisie.add_exercise(student_sara, classes_exercise)
instructor_andy.add_exercise(student_matt, classes_exercise)


# Create a list of students. Add all of the student instances to it.
students = list()
students.append(student_matt)
students.append(student_bruce)
students.append(student_kub)
students.append(student_mike)
students.append(student_sara)

# Create a list of exercises. Add all of the instances to it.
exercises = list()
exercises.append(list_exercise)
exercises.append(multiple_inheritance_exercise)
exercises.append(interface_exercise)
exercises.append(function_currying)
exercises.append(classes_exercise)
exercises.append(dictionaries_exercise)


# For Each Student, list all exercises they were assigned
# interate students and turn into dict to extract the exercises list() property off object
for student in students:
    student_dict = student.__dict__
    exercises = student_dict["exercises"]

    # Creating new set and using that so no duplicates
    new_set = set()
    for exercise in exercises:
        new_set.add(exercise.__dict__["name"])

    # if only one list that, if more separate with comma and "and"
    list_of_exercises = ", and ".join([", ".join(list(
        new_set)[:-1]), list(new_set)[-1]] if len(list(new_set)) > 2 else list(new_set))

    print(f"{student_dict['first_name']} is working on {list_of_exercises}")

'''
Matt is working on Lists, and Classes
Bruce is working on Interfaces
Kub is working on Function Currying
Mike is working on Multiple Inheritance
Sara is working on Classes
'''
