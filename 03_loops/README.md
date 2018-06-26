# Loops 

A loop is a way to call on items in a list one at a time

##_For_ loops

```python
student_names = ['Ann', 'Liza', 'George']

for name in student_names:
    print(f"Name ->{name}")
```
>Name -> Ann \
Name -> Liza \
Name -> George

Here, we've made a list of "Student names", and a for loop that will print every name in the list one by one. You can read it as _"for every 'name' in 'student_names', print "Name -> " and their name"_. The "name" in the loop is a temporary variable that holds whatever value the loop is currently on. 

###The _Range_ Function

By default, a loop with start in Index value 0 of a list, go till the end, an dhave a step/increment of 1. You can change this with the range function.
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

### Breaks


