# Dictionaries

Dictionaries are like lists, except they are used to store key-value-pairs. 

In a dictionary, each element has a key and a value (unlike a list which only has values). A key and a value make a key-value-pair. 
The value can be of any type, just like in lists, without you defining it. You can even have nested dictionaries, where a key's value is a whole different dictionary. Typically a key is anything that can be uniquily represented, like a string, and not a Boolean.

Here is an example of a dictionary. The strings and ints on the left are the keys, and on the right are the values.

```python
student = {
    "name": "Mark",
    "student_ID": 12345,
    "1": "number",
    "failing": None
}
```
>{'name': 'Mark', 'student_ID': 12345, '1': 'number', 'failing': None}

***

If you want, you can group multiple dictionaries together in a list. Notice how the list still uses square brackets.

```python
all_students = [
    {"name": "Mark", "student_ID": 12345,},
    {"name": "Katy", "student_ID": 67890},
    {"name": "Ann", "student_ID": 13579}
]
```
>[{'name': 'Mark', 'student_ID': 12345}, {'name': 'Katy', 'student_ID': 67890}, {'name': 'Ann', 'student_ID': 13579}]

***

## Calling on Values or Keys

To get to a value in a dictionary, use the key as you would an index in a list.

```python
print(student["name"])
```
>Mark

And if you want to get to a value in a dictionary that's in a list, specify the list first, and then call on the key.
```python
print(all_students[1]["name"])
```

>Katy

If you try and access a value that does not exist, Python will raise the exception "KeyError""

```python
print(student["last_name"])
```
>KeyError: 'last_name'

If you want to avoid the exception, you can have Python return a specified value for the key. This won't change anything in your dictionary itself, only what Python returns when you try and call on that key.

```python
print(student.get("last_name", "Unknown"))
```

>Unknown

A note on the "get" function. This does the same thing as the square brackets we have been using so far. The square brackets are just an "operator" or "alias" for the get function, just like the plus sign is an operator for the "add" function. The only difference is that you can add more parameters with the get function, like we did above.

If you want to, you can call on all the keys or all the values in a dictionary with ".keys()" or ".values()"

```python
print(student.values())
print(student.keys())
```
>dict_values(['Mark', 12345, 'number', None]) \
dict_keys(['name', 'student_ID', '1', 'failing'])

***

Changing and deleting values is done the same way as in lists. By the way, using the "del" function deletes the entire key-value-pair.

```python
student["name"] = "James"
print(student["name"])
```

>James

```python
del student["name"]
print(student["name"])
```

>KeyError: 'name'

## Exercise wih Dictionaries and Lists

Here, I  played around with dictionaries and lists. I listed out my dad's side of the family, and wrote code that was about my position in the family.

```python
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


print("I am " + family["children"][1]["child1"])

print("My brothers are " + family["children"][0]["child1"] + ", " + family["children"][0]["child2"] + ", and " +
      family["children"][2]["child1"])
```

>I am Liza \
My brothers are Joe, Kunju, and Manas