# Functions

A function is a reusable block of code that you can use to avoid repetition and increase organization in your code. Basically, a function is a set of predetermined instructions that can take in and / or return values. Python comes with a bunch of preset functions, like `print()`, but you can make your own if you want.

A function that you make has two parts - the header and the body. In the header, enter the `def` keyword, the name of your function, and a colon. The second part is the function body, below the header - this is where you can write your code.  If you want to include arguments / parameters for your function, write the function arguments in parenthesis after the name, as shown below. You can use these arguments in your function body like variables, and they will be inaccessible from the rest of your code, outside the function. Make sure that each function does only one thing. When using your function, use like a preset function - type out the name, and make sure you enter in the correct number of arguments in the right positions. Just to be clear, parameters are the values you enter while defining the function, and arguments are what you enter when using, or calling, the function.
## Creating your own Functions
```python
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


def add_student(name, age):
    new_student = {
        "name": name,
        "age": age
    }
    students.append(new_student)

print(students)

add_student("Liza", 15)

print(students)
```
>[{'name': 'Mark', 'age': 15}, {'name': 'Emily', 'age': 14}, {'name': 'Joseph', 'age': 15}] \
[{'name': 'Mark', 'age': 15}, {'name': 'Emily', 'age': 14}, {'name': 'Joseph', 'age': 15}, {'name': 'Liza', 'age': 15}]

So a quick breakdown of what I've done above. First, I made a list of dictionaries, each dictionary representing a student in a pretend classroom, with the keys of "name" and "age". Then I created the function `add_student` which has two arguments / parameters - name and age. I then wrote code that would create a new dictionary representing a student whenever the function was called. And then I tested out the function. You can see I printed out the student list, and the result included Mark, Emily and Joseph. Then I called on the `add_student` function, input the name and age I wanted, and when I printed the list a second time, Liza and her age was now in it. 


A note on the `return` keyword. It does just that - it returns to you whatever data you have specified to be used again later on. The difference between `return` and `print` is that the print function doesn't store any data - if you tried setting a variable to the data of a function that only prints something, the variable wouldn't be holding anything. However, if the function *returns* something, your variable will now hold the result of whatever process you had in the function. Here's an example below:

```python
def add_these_two_numbers(number1, number2):
    return number1 + number2


print(add_these_two_numbers(2, 5))
```
>7

Also, when used in a function, the `return` statement leaves the function once the interpreter executes it. 

```python
def my_function():
    print("Before return. This will be printed.")
    return
    print("After return. This won't be printed.")

```

### Default Arguments

Remember, typically when using a function, you have to enter in all of the required arguments, But you if want to make an argument optional - so if it's entered, that's great, and if not you will input something *default* or preset - you can use *default arguments*. To use it, simply add an equal sign and your default value in the function header as shown below.
```python
def add_student(name, age=15):
    new_student = {
        "name": name,
        "age": age
    }
    students.append(new_student)

add_student("Liza")
```

Now, even though I didn't specify Liza's age, her dictionary will contain the default age - 15. If I did specify her age with something other than 15, the default value will be overridden, and her dictionary will have the correct value. 

### Named Arguments

For the sake of clarity to developers, you can use *named arguments*, where you just specify what the value you're entering is. 

```python
def add_these_two_numbers(number1, number2):
    return number1 + number2


print(add_these_two_numbers(number1=2, number2=5))
```
>7

It makes no difference in what actually happens and what the computer does, it just makes it easier for developers. 

### Variable Arguments

Have you noticed that for functions like the `print` function, there is no limit to the number of arguments you can enter? You can make functions like this using variable arguments. Just add the text `*args` as a parameter, and use is like normal in the body without the asterisk.

```python
def my_print(value, *args):
    print(value)
    print(args)


my_print("yo", "hey", "there", True, None, 15, "Thanks for reading this stuff!")
```
>yo \
('hey', 'there', True, None, 15, 'Thanks for reading this stuff!') 

You can see how "yo", because of its position, is representing the parameter "value". If you want, you can have a function with just the  `*args` parameter on its own. You can also enter anything as the arguments here, like ints, strings, booleans, etc..

## Nested Functions

If you want to have functions inside other functions, to reduce repetition, you can. Remember, you can't call the nested function from outside the nesting function. But if the nesting function has a variable or function, you can reach it from the nested function. For example;

```python
def nesting_function():
    variable = "The example variable"

    def nested_function_1():
        print("The example function")

    def nested_function_2():      # This is another example function
        print("Here I can use", variable)
        nested_function_1()
        
    nested_function_2()
```
>Here I can use The example variable\
The example function


---

By the way, there's a subject I don't fully understand yet, but I noticed it and wanted to mention it here;

This doesn't work, because foobar is defined below the call for foo().
```python
def foo():
    print("foo")
    bar()
    foobar()
    
def bar():
    print("bar")
    
foo()
    
def foobar():
    print("foobar")
```

This does work, even though the definition of bar() and foobar() are underneath the definition of foo(), because everything is above the call for foo*().

```python
def foo():
    print("foo")
    bar()
    foobar()
    
def bar():
    print("bar")
    
def foobar():
    print("foobar")
    
foo()
```

## Lambda Functions

Another way to create function, without the `def` keyword, for when you want to save a little bit of time and effort. They work when the function body would be really simple, a single line of code. Here's an example;

This is a function I made that will just take an input and return that input doubled.
```python
def double(x):
    return x * 2
```

Here, I'm making that same function, but using the `lambda` keyword. Notice how I don't need the `def` or `return` keywords here. 
```python
double = lambda x: x * 2
```

I would call on both of these functions the exact same way (`double(x)`).