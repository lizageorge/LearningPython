answer_add_student = input("Do you want to add a student? Answer 'yes' or 'no' ")

student_list = []


def add_student(name, age):
    student = {"name": name, "age": age}
    student_list.append(student)


while answer_add_student == 'yes':
    student_name = input("What's the student's name? ")
    student_age = input("What's the student's age? ")
    student_name = student_name.title()
    add_student(student_name, student_age)
    answer_add_student = input("Do you want to add another student? Answer 'yes' or 'no' ")

print(student_list)
