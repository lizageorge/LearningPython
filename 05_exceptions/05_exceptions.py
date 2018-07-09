student = {
    "name": "Mark"
}

""" I'm commenting this line out so that the rest of the code will run
print(student["last_name"])
"""

try:
    print(student["last_name"])
except KeyError:
    print("Error finding last_name")


try:
    number = 3 + student["name"]
except TypeError as error:
    print("Error adding a string and integer")
    print(error)

print("This code executed!")