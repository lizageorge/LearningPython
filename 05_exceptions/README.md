# Exceptions 

Exceptions are errors that occur during the program execution that cause the program to stop executing. Usually, there's an error somewhere, and the computer doesn't know what to do. So the program will crash. When working with IDEs like Pycarm, you should get the text "Process finished with exit code 0" whenever you don't have any exceptions. If the text says "Process finished with exit code 1", the program has failed.

To handle Exceptions, we us Exception Handling, where we use the *try* and *execute* blocks, like shown below.

```python
try:
    print(student["last_name"])
except KeyError:
    print("Error finding last_name")
    
print("This code executed!")
``` 

> Error finding last_name \
This code executed!

There are many different kinds of exceptions, and if you want to be thorough, you would add, or "chain", a differetn except block for each type. There's also a generic *Eception* type that you can use, but it isn't recommended because you can't find out what actually went wrong and what to fix. Also, you'll notice when handling exceptions that the messages that Python gives you disappear. To fix this, simply add on the *add error* code as shown below.
By the way, the code below also shows an example of a different type of Exception, the TypeError exception.

```python
try:
    number = 3 + student["name"]
except TypeError as error:
    print("Error adding a string and integer")
    print(error)

print("This code executed!")
```

>Error adding a string and integer \
unsupported operand type(s) for +: 'int' and 'str' \
This code executed!


Exeption Handling is used normally wherever you think the code is likely to crash. For example, anywhere there is User Interaction. 