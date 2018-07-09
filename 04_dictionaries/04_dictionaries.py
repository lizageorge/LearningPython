student = {
    "name": "Mark",
    "student_ID": 12345,
    "1": "number",
    "failing": None
}

print(student)

all_students = [
    {"name": "Mark", "student_ID": 12345,},
    {"name": "Katy", "student_ID": 67890},
    {"name": "Ann", "student_ID": 13579}
]

print(all_students)

print(student["name"])

print(all_students[1]["name"])

""" I commented this out so that the rest of the code would work
print(student["last_name"])
"""

print(student.get("last_name", "Unknown"))

print(student)

print(student.values())
print(student.keys())

student["name"] = "James"
print(student["name"])

""" I commented this out so that the rest of the code would work
print(student["last_name"])
del student["name"]
print(student["name"])
"""

"""
This is the exercise I did with dictionaries and lists
"""

family = {
    "father": "Kunjachan",
    "mother": "Alice",
    "children": [
        {
            "father": "Sherry",
            "mother": "Archana",
            "child1": "Joe",
            "child2": "Kunju"
        },
        {
            "father": "George",
            "mother": "Anu",
            "child1": "Liza",
        },
        {
            "father": "Manu",
            "mother": "Ancy",
            "child1": "Manas",
            "child2": "Mili"
        }
    ]
}
print(f"family = {family}")

"I am {Liza}"

print("I am " + family["children"][1]["child1"])
"My brothers are Joe, Kunju and Manas"

print("My brothers are " + family["children"][0]["child1"] + ", " + family["children"][0]["child2"] + ", and " +
      family["children"][2]["child1"])
