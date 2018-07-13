# Files

## Opening, Reading, and Writing into Files

When using the `open()` function to open files, write in the file name and the access mode. The access modes are "a" to append (or add text to the file), "r" to read, and "w" to write". There are more, but this is all I know so far. By the way, keep in mind that using the write mode erases everything that was previously in the file. There's also a `readLines()` function that will make a list of everything in a list, with what's in each line as an object.

```python
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
```
The first time I run the program:
>The file doesn't exist / have anything in it yet.\
Do you want to add a student? Answer 'yes' or 'no' 

After I enter some values;
>The file doesn't exist / have anything in it yet.\
Do you want to add a student? Answer 'yes' or 'no' *yes*\
What's the student's name? *liza*\
Do you want to add another student? Answer 'yes' or 'no' *yes*\
What's the student's name? *ann*\
Do you want to add another student? Answer 'yes' or 'no' *yes*\
What's the student's name? *george*\
Do you want to add another student? Answer 'yes' or 'no' *no*\
['Liza\n', 'Ann\n', 'George\n']

If I run the program again;
>['Liza\n', 'Ann\n', 'George\n']\
Do you want to add a student? Answer 'yes' or 'no'

And I also have a file in my folder called "student_names.txt", which contains;
>Liza\
Ann\
George 