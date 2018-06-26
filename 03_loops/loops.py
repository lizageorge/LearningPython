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

x = 0
while x < 10:                   # example of a while loop
    x += 1
    print(f"Number is {x}")

print("\n----------\n")

num = 10
while True:
    if num == 20:
        break
    print("This is going to be repeated over and over and over...")