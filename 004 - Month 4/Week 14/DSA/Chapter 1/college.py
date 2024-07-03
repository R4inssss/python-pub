#! python3
#       college.py | dsa chapter 1 exercise
#       class hierarchy for people in a college campus (staff, faculty, students)

import sys


# college main
class college:
    def __init__(self):  # Just here to get the code to work
        pass

    def get_label(self):  # Just here to get the code to work
        return "College"


# staff
class staff(college):
    def __init__(self):
        super().__init__()
        self.staff_types = {"Dean": '', "President": '', "Clerk": '', "Office": ''}

    def types(self):
        for role in self.staff_types.keys():
            print(self.staff_types.keys())
            data = input(f'Insert your staff member data for {role}: ').split()
            if data and role not in self.staff_types:
                self.staff_types[role] = data
                print(self.staff_types)
            else:
                print(f"Error: Invalid data or {role} already exists.")
                return False


# students
class student(college):
    def __init__(self):
        super().__init__()
        self.student_type = {"Freshman": '', "Sophomore": '', "Junior": '', "Senior": ''}

    def types(self):
        for role in self.student_type.keys():
            print(self.student_type.keys())
            data = input(f'Insert your student member data for {role}: ').split()
            if data and role not in self.student_type:
                self.student_type[role] = data
                print(self.student_type)
            else:
                print(f"Error: Invalid data or {role} already exists.")
                return False


# teacher
class teacher(college):
    def __init__(self):
        super().__init__()
        self.teacher_type = {"History": '', "Math": '', "English": '', "Science": ''}

    def types(self):
        for role in self.teacher_type.keys():
            print(self.teacher_type.keys)
            data = input(f'Insert your teacher member data for {role}: ').split()
            if data and role not in self.teacher_type:
                self.teacher_type[role] = data
                print(self.teacher_type)
            else:
                print(f"Error: Invalid data or {role} already exists.")
                return False


# menu
def menu():
    college_instance = college()
    staff_instance = staff()
    student_instance = student()
    teacher_instance = teacher()

    options = {'1': staff_instance.types,
               '2': student_instance.types,
               '3': teacher_instance.types,
               }

    while True:
        print("\nMenu:")
        print("1. Enter staff data")
        print("2. Enter student data")
        print("3. Enter teacher data")
        print("4. Exit")

        choice = input(f"Enter your choice: ")
        if choice in options.keys():
            options[choice]()
        else:
            sys.exit('Goodbye.')


if __name__ == "__main__":
    menu()
