students = [
    {
        "name": "Mark",
        "age": 15
    },
    {
        "name": "Emily",
        "age": 14
    },
    {
        "name": "Joseph",
        "age": 15
    }
]


def add_student(name, age=15):
    new_student = {
        "name": name,
        "age": age
    }
    students.append(new_student)


print(students)

add_student("Liza")

add_student("Acha", 43)

add_student(name="Amma", age=40)

print(students)


def add_these_two_numbers(number1, number2):
    return number1 + number2


print(add_these_two_numbers(2, 5))


def my_print(value, *args):
    print(value)
    print(args)


my_print("yo", "hey", "there", True, None, 15, "Thanks for reading this stuff!")


''' I'm commenting this out for convenience
print("-------------------")

user_name = input("Please enter *your* name here: ")
print("The user's name is ", user_name)
'''

print("-------------------")


def nesting_function():
    variable = "The example variable"

    def nested_function_1():
        print("The example function")

    def nested_function_2():      # This is another example function
        print("Here I can use", variable)
        nested_function_1()

    nested_function_2()


nesting_function()

