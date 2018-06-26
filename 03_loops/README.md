# Loops 

A loop is a way to call on items in a list one at a time

## _For_ loops

The *for* loop is the first kind of loop. 
```python
student_names = ['Ann', 'Liza', 'George']

for name in student_names:
    print(f"Name ->{name}")
```
>Name -> Ann \
Name -> Liza \
Name -> George

Here, we've made a list of "Student names", and a for loop that will print every name in the list one by one. You can read it as _"for every 'name' in 'student_names', print "Name -> " and their name"_. The "name" in the loop is a temporary variable that holds whatever value the loop is currently on. 

### The _Range_ Function

By default, a loop will start in Index value 0 of a list, go till the end, an dhave a step/increment of 1. You can change this with the range function.
\

The Range function returns a list that can be iterated. It has three parameters; the minimum /starting index value, the maximum/ending index value, and the incrememnt/step. But the number of parameters you specify changes which parameter each of your values corresponds to.
* 1 parameter = `range(max. index value)`
* 2 parameters = `range(min.index value, max. index value)`
* 3 parameters = `range(min.index value, max. index value, step)`

*Note: whatever index number you enter *will not be included* in your final list. \
Here's an example of a for loop that uses the range function:

```python
for index in range(0, 11, 2):
    print(index)
```
>0\
2\
4\
6\
8\
10

If you don't specify any lists, thr function will work on a list of all whole numbers and 0. 

### The *Break* keywords

The *Break* keyword is a way to stop a *for* loop from executing when a certain condition is met, and will instead exit it.

Say we were going through a list of 0 - 10, looking for 5. If we just used a for loop (like shown below), the loop would continue to run even after finding 5.
```python
for index in range(11):
    if index == 5:
        print('Found 5!')
    print(f'{index}, searching for 5.')
```
>0, searching for 5.\
1, searching for 5.\
2, searching for 5.\
3, searching for 5.\
4, searching for 5.\
Found 5!\
5, searching for 5.\
6, searching for 5.\
7, searching for 5.\
8, searching for 5.\
9, searching for 5.\
10, searching for 5.

To be more efficient, we can insert the *break* keyword. This will make the computer leave the *for* loop entirely, and continue on to whatever code is after it.

```python
for index in range(11):
    if index == 5:
        print('Found 5!')
        break
    print(f"{index}, searching for 5.")
```

>0, searching for 5.\
1, searching for 5.\
2, searching for 5.\
3, searching for 5.\
4, searching for 5.\
Found 5!

### The *Continue* keyword

The *Continue* keyword is a way to skip a value in a list when a certain condition is met.

Say we're still working with that list of 0-10, but this time, we want all the value to printed *except* 5. To do this, we would insert the *continue* keyword as shown below. This wll make the computer skip whatever code is after the keyword in the loop, and move on to the next index.

```python
for index in range(11):
    if index == 5:
        continue
    print(index)
```

>0\
1\
2\
3\
4\
6\
7\
8\
9\
10\
11

Now we have a list of 0-10, skipping 5!

## While Loops

The *while* loop is the second kind of loop. It will let a section of code run over and over again, as long as a certain condition is met. The *Break*  and *Continue* keywords will work just like the do in *for* loops.

For example, this loop will run on and on until x becomes greater than 10.

```python
x = 0
while x < 10:              
    x += 1
    print(f"Number is {x}")
```
>Number is 0\
Number is 1\
...\
Number is 8\
Number is 9

And this one is an example of an *Infinity Loop*; it will keep on running forever, unless we insert a break 

```python
num = 10
while True:
    if num == 20:
        break
    print("This is going to be repeated over and over and over...")
```