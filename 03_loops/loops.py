# example of for loops

student_names = ['Ann', 'Liza', 'George']

for name in student_names:
    print(f"Name ->{name}")

print("\n----------\n")

# use the range function

for index in range(0, 11, 2):       # starting at 0 till 10 and increasing by 2
    print(index)

print("\n----------\n")

for index in range(11):             # using the break keyword
    if index == 5:
        print('Found 5!')
        break
    print(f"{index}, searching for 5.")

print("\n----------\n")

for index in range(11):         # using the continue keyword
    if index == 5:
        continue
    print(index)

print("\n----------\n")

