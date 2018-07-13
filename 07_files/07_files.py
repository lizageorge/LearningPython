
def save_student_into_file(student_name):
    student_names = open("student_names.txt", "a")
    student_names.write(student_name + "\n")
    student_names.close();


def read_student_names():
    student_names = open("student_names.txt", "r")
    print(student_names.readlines())


try:
    read_student_names()
except Exception:
    print("The file doesn't exist / have anything in it yet.")

answer_add_student = input("Do you want to add a student? Answer 'yes' or 'no' ")


while answer_add_student == 'yes':
    student_name = input("What's the student's name? ")
    student_name = student_name.title()
    save_student_into_file(student_name)
    answer_add_student = input("Do you want to add another student? Answer 'yes' or 'no' ")

read_student_names()