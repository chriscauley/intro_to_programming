Intro to Programming Day 3
========

## A better room program

Let's start by finisihing up the above program to fit the final exercises from last time. Look at the solution in room4.py

```python
def number_input(question):
    """ Just like raw_input, but forces a number and returns an integer """
    while True:
        input = raw_input(question)
        if input.isdigit():
            break
        else:
            print "Invalid input. Please enter a number."
    return int(input)

def dict_input(options,question):
    """ Just like raw_input, only it only accepts options printed from a dict """
    num_options = len(options)
    i = 1
    print question
    for option in options:
        print str(i) + "-" + option
        i = i+1
    while True:
        answer = raw_input("Select an option (1-"+str(num_options)+"): ")
        if answer.is_digit():
            if int(answer) > 0 and int(answer) <= num_options:
                return options[int(answer)]

def get_room():
    length = number_input("What is the length of the room?")
    width = number_input("What is the width of the room?")
    height = number_input("What is the height of the room?")
    
    perimeter = 2 * int(length) + 2 * int(width)
    wall_area = perimeter * int(height)
    floor_area = length * width # also the ceiling_area!
    
    amounts = {
        "trim": perimeter,
        "paint": (wall_area + floor_area) / 350, #assuming 350 sq ft per gallon of paint
        "carpet": floor_area,
        "wall_sockets": perimeter/15, #Q1
        }
    return amounts

def price_room(room,print_prices):
    prices = {
        "trim": 3, #$/ft
        "paint": 20, #$/gallon
        "carpet": 30, #$/sq ft
        "wall_sockets": 40 #$/socket, #Q1
        }
    
    estimates = {}
    
    total = 0
    for key in room:
        estimates[key] = prices[key]*room[key]
        if print_prices:
            print key.upper() + " estimate: $" + str(estimates[key])
        total = total + estimates[key]
    return total

enter_room = 'y'

rooms = []
while True:
    if enter_room == 'y':
        rooms.append(get_room())
    elif enter_room == 'n':
        break
    else: 
        print "Invalid input, try again."
    enter_room = raw_input("Would you like to enter another room? (y/n) ")

total = 0
for room in rooms:
    total = total + price_room(room,False)

print "Final total: $"+str(total)
```

Here we've broken most of the program into two functions, get_room and price_room. `get_room` creates a dictionary describing the cost of a room (a "room object", if you will) from a series of user inputs. `price_room` Takes in the output from `get_room` and returns the total cost of the room. The program defines a series of functions (a library of code) and then executes a while loop that uses these functions to do math and generate an output.

## Importing and Building Libraries

If you had to keep everything in one file, programs would quickly unmanageable. As you see above this has become many pages worth of code, which becomes unmanageable and unreadable as it grows. So instead we prefer to break up things into various files. All of the functions that we have created so far has been placed in a file called `utilities.py`. Download this to the same directory that python runs from (for windows this is `C:\Python`, on Mac and Linux you can just save it to your home folder). Then in the a separate file in the same directory (or in a prompt) you can import things three different ways.

* Import an individual object with `from some_library import something`.

```python
from utils import add3
print add3(1,2,3) # 6
```

* Import the library itself like `import some_library`. Afterwards you can use the contents of the library like `some_library.some_object`

```python
import utils
print utils.add3(1,2,3) # 6
```

* Import everything from a library. Here the asterix `*` is used to indicate that you want to import everything. This should not be used in files since you may have trouble figuring out what you imported from where later on. Also, is this library has variables or functions of the same name as variables you have made they will e overwritten.

# import everything from the library
from utils import *
print utils.add3(1,2,3) # 6
```

Very large programs need to be better organized using directories. Look at the `room_builder` folder.

<!!--- MISSING!!!!! -->

## Built in and third party libraries

As I said the first day, python is a "Batteries Included" language, meaning that most common programming problems are solved by the many built in libraries. Additionally there is an even more impressive set of third party libraries that solve complex problems very efficiently. If you want to gain a mastery over python, I recommend studying the [Python Module of the Week](http://pymotw.com/2/contents.html) website which covers almost all of the python basics in depth.

### `random`

Getting random values is essential to writting many programs, whether it is to create random strings for encryption or generate random values for games. `random.randint(n1,n2)` gives a random number between two values (inclusive). `random.random()` gives a random number between 0 and 1. `random.choice(some_list)` gives a random value from a list. The following two examples both do the same thing, return a random number between 1 and 6 (as if rolling a dice).

```python
import random

dice1 = random.randint(1,6)
dice2 = random.choice(range(1,7))
```

#### Exercises

1. Write a program that picks a random number between 1 and 10 and then asks the user to guess that number. Be sure to use `number_input` (imported from utils.py) to ensure they pick a valid number. If the user is wrong, inform them if the random number is higer or lower than their guess.

2. Put the above in a `while` loop. Keep track of how many guesses they make and tell them "It took # guesses" when they get the right answer.

### `datetime`

With oddly numbered months, leap years, and daylight savings programming dates can be a real pain. Luckily there is the builtin `datetime` library that handles all the trickey math. There are 4 main data types:

* `datetime.date` - A date that is unaware of time.

* `datetime.time` - A time of day.

* `datetime.datetime` - A combination of the previous two data types.

* `datetime.timedelta` - The difference between two of the above objects.

We'll focus only on the `datetime.datetime` and `datetime.timedelta` objects. A `datetime.datetime` requires three integers for year, month, day and can take optional arguments for hour, minute, second and microseconds. A `datetime.timedelta` object requires days and has two optional arguments for seconds and microseconds. The following example shows how to find the difference between two `datetime.datetime`s.

```python

import datetime as dt # a nice trick to save characters and to avoid confusion.

my_birthday = dt.datetime(1983,6,20) #June 20,1983
now = dt.datetime.now()

my_age = now-my_birthday # a timedelta object

print "I am " + str(my_age.days/365) + " years and " + str(my_age.days%365) + " days old."

#how many days are in a billion seconds?
num_days = 1000000000 / (60*60*25)
datetime_billion = dt.timedelta(num_days) + my_birthday
print "I'll be a billion seconds old on " + str(datetime_billion)
days_to_billion = (datetime_billion - dt.datetime.now()).days
print "That is in " + str(days_to_billion) + " days"
```

#### Exercises

1. Change the above program to ask the user what their birthday is. Be sure to use `number_input` again and ask them the year, month, and date they were born.

2. Modify the above program (or anything you have written) to record two times, one at the begining and one at the end of the program. When then inform the user how long the program took to run.

## Saving and loading

Files can be read and written using `open`, which returns a file object. `open` takes in two aguments, the file path and the mode which is a string containing any of the following characters: 'r' (read), 'w' (write), or 'b' (binary, don't worry about this for now).

```python
f = open('rhyme.txt','w') #file does not exist, it will be deleted if it does!
f.write("Mary had a little lamb")
f.write("her fleece was white as snow")
f.close()

#open the file in a text editor to verify the change

f = open('rhyme.txt','rw') #read+write, won't delete file contents
more_lines = [
    "everywhere that mary went",
    "her lamb was sure to go"
]
f.writelines(more_lines) #convenient short cut
f.close()
```

Try this on your own and open the file. You'll notice that the file rhyme.txt has no line breaks, this is because you need to include "\n" at the end of every line (this is an "escape character" for a line break).

## Errors

Writting error free programs is nearly impossible. You can't always see every possible input or eventuality. You can even declare that an error has occurred to stop the current flow of the program. This is referred to as "raising an exception". We've seen errors before when an improper value is entered into a type function.

```python
>>> int("I'm not a number I am a human being!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'I\'m not a number I am a human being!'
```

This tells us where the error occurred (In this case "stdin" or "standard input" which is the terminal. This can be used to hunt down the file in which the error occurred. Then it tells us the type of error (in this case a `ValueError`) and why it occurred.

You can use then reverse this so that the program isn't halted when an error occurs:

```python
while True:
    answer = raw_input("Enter a number: ")
    try:
        answer = int(answer)
        break
    except ValueError:
        print "Invalid answer, try again."
```

This is an alternative method to the previous `number_input` seen last week. The code within the `try` block is executed and if a `ValueError` occurs the code inside the `except` block is executed. Otherwise the `except` block is ignored. If you leave out the `ValueError` it will catch all errors of every type. This is generally bad practise because it can lead to unforseen errors being ignored.

When your program becomes complex you might want to raise your own errors. Let's say you have an accounting program that is very complex. Even though it is thoroughly tested you may still want to include error checks. If, when all calculations are complete, 
