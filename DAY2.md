Intro to Programming Day 2
========

## A few string methods

Last week we asked for a `raw_input` where we wanted a number. If the user enters an invalid value, the trying to turn the input into an integer results in a `ValueError`.

```python
>>> some_number =raw_input("Enter a number: ")
Enter a number: a
>>> print some_number
a
>>> int(some_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
```

What we want is a function that checks to see if `some_number` is a number. As you can imagine, if there was a built in function for everything we could want to do for a string then it would be impossible to memorize all the built in functions and naming variables would become very difficult. Instead a string has a variety of "memthods". Think of these as functions that automatically use the string as an argument.

```python
>>> not_a_number = 'a'
>>> a_number = '1'
>>> not_a_number.isdigit()
False
>>> a_number.isdigit()
True
```

If there was a function `isdigit` you would write `isdigit(some_variable)`, but all strings have a method `isdigit` which determines if the string can be turned into an `int` and returns `True` or `False` accordingly.


To see all of the methods of a string we can use the `dir` built in function, which prints a list of all possible methods of the variable. `dir` will always show the same thing for any two strings, but will return a different list of methods for a different type.

```python
>>> print dir('a')
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__',
'__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', 
'_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print dir([1,2])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', 
'__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__',
'__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

Looking at this we can see many useful methods for strings and lists. I'll briefly describe a few of these. We'll ignore the "magic methods" or those starting with underscores, "_". These are advanced and outside the scope of this class. Don't worry about memorizing this list just yet. This is mostly just to give you an idea of what each method can do.

```python
>>> some_string = "This is a string"
>>> print some_string.lower()
this is a string
>>> print some_string.upper()
THIS IS A STRING
>>> print some_string.title()
This Is A String
>>> print some_string.startswith('z')
False
>>> print some_string.startswith('T')
True
>>> print some_string
this is a string
```

And now their definitions:

* `str.lower()` - return the string with all letters lowercase.

* `str.upper()` - return the string with all letters uppercase. 

* `str.title()` - return the string with the first letter of every word capitalized.

* `str.startswith(string)` - takes in a string as an argument and returns `True` or  `False` depending on whether or not the string starts with the string argument.

* The last line is to illustrate that the string has not changed

And now some `list` methods:

```python
>>> a_list = range(3)
>>> print a_list
[0,1,2]
>>> a_list.append("monkey")
>>> print a_list
[0,1,2,"monkey"]
>>> a_list.insert(1,666)
>>> print a_list
[0,666,1,2,"monkey"]
```

And now the definitions:

* `list.append(variable)` - adds the variable to the end of the list. This increases the length of the list by one.

* `list.insert(position,variable)` - inserts the variable at the position. This will increase the length of the list by one.

* Notice that neither of these return a value. Instead the variable a_list itself is changed. This is very different then the methods of a string.

## `While` loops and advanced flow control

Let's go back to the original problem stated at the begining of the last problem. We want to insure that a value taken in by `raw_input` is a number. You could do something like this:

```python
a_string = 'not a number'
for i in range(1000):
    if not a_string.isdigit():
        a_string = raw_input("Enter a number: ")

a_number = int(a_string)
```

This will start by setting a variable (`a_string`) to a value that is not a number (because `a_string.isdigit() == False`) and then run a for loop 1000 times. If `a_string` is not a number (as it is at the start) it will ask for a number via `raw_input`. Once they enter a number, the loop will repeat indefinitely until they enter a number. Although the loop isn't doing anything, it still takes a small time to run and slows down the program. Additionally future programmers might not be able to figure out what you're doing very easily.

It'd be much better to use a `while` loop.

```python
length = raw_input("Enter a number: ")
while not length.isdigit():
    length = raw_input("No, a number dummy: ")

length = int(length)
```

Here, if the user enters a number the first time, then `not length.isdigit()` will be false and the `while` loop will not execute. If they enter a non-number for the length, the while loop will repeat until they enter a valid value. We could change the question depending on how many times it has been asked:

`while` loops have the syntax `while conditional_statement:`, where the conditional statement can be an expression, like `while i < 10000:`, or even a variable like `while keep_dancing`. A `while` loop works very similar to a `for`, only a `for` loop cycles through values and a `while` loop executes the code, checkes the conditional, and then repeats if the conditional is still `True`. As long as the conditional statement evaluates to `True`, the code intedented after the `while` loop cycles forever.

A more practical conditional would be something like `while number_of_lives > 0:` for a video game or maybe `while heightest_piece_height < 20:` for something like Tetris.

   Most programs use something like `while True:` so that the program loops indefinitely until the loop is manually proben. You can manually break out of the normal flow of any `while` or `for` loop using two key words, `break` and `continue`. `break` means you want to exit the loop entirely. This is useful when there are many reasons to exit a `while` loop or when you are looking for a matching value in a list. `continue` ignores the rest of the `while` loop, checks the conditional, and restarts the loop. If you wanted to give someone three chances to guess a password you could do this.

```python
guesses = 0
knows_password = False
while guesses < 3:
    password = raw_input("What is the password: ")
    if password == "Rumplestiltskin":
        print "That's correct!"
        knows_password = True
        break
    if len(password) == 0:
        # They didn't enter anything, don't hold it against him
        print "You didn't enter anything."
        continue
    guesses = guesses + 1
    print "Wrong password, try again. You have " + str(3-guesses) " guesses left."

if knows_password:
    print "Welcome!"
    # the rest of the program
else:
    print "Unathorized login attempt. This computer will self-destruct in 10 seconds."
```

If the password is entered correctly, we `break` out of the `while` loop rather than executing the remaining code. If they don't enter a password we aren't going to hold it against them, so we `continue`, which jumps to the top of the while loop and ignores the `guesses = guesses + 1` statement.

### Exercises

1. Write a while loop that prints the numbers 0-10. 

2. What would be the loop conditional for the following games: Chess, Checkers, Hot Potato, Calvin Ball, Candy Land? If you don't know some of these, feel free to pick any board or video game and answer the question.

2. What does the following program do? Can you change this to print the 1000 verses? (I don't recommend executing it) Could you have done this with a `for` loop? Can you change the lamb chops program to print indefinitely? Could you have done this with a `for` loop? (I really don't recommend executing this program)


```python
i = 0
while i < 10:
   print "This is the song that doesn't end."
   print "And it goes on and on my friend."
   print "Some people started singing it not knowing what it was."
   print "And they'll continue singing it forever just because..."
   i = i + 1
```

## Bringing it all together: an interlude

Last time we learned a variety of data types and syntax for python. For this session we're going to learn functions, libraries, exceptions, and dictionaries. To do this we're going to understand the following problem and then improve on it with these new techniques

Imagine that you're writting programs to estimate the amount of materials required to a remodel room. To do this we'll need to know the perimeter of a room, floor area, wall area. This can then be converted to gallons of paint, sheets of sheetrock, feet of trim and crown molding, and square feet of carpet or hard wood. So we start with a simple program like this:


```python
length = raw_input("What is the length of the room?")
width = raw_input("What is the width of the room?")
height = raw_input("What is the height of the room?")

perimeter = 2 * int(length) + 2 * int(width)
wall_area = perimeter * int(height)
floor_area = length * width # also the ceiling_area!

amount_of_trim = perimeter
amount_of_paint = (wall_area + floor_area) / 350 #assuming 350 sq ft per gallon of paint
amount_of_carpet = floor_area

price_of_trim = 3 #$/ft
price_of_paint = 20 #$/gallon
price_of_carpet = 30 #$/sq ft

trim_estimate = price_of_trim * amount_of_trim
paint_estimate = price_of_paint * amount_of_paint
carpet_estimate = price_of_carpet * amount_of_carpet

print "Trim estimate: $" + str(trim_estimate)
print "Print estimate: $" + str(print_estimate)
print "Carpet estimate: $" + str(carpet_estimate)
print "Total estimated cost: $" + str(trim_estimate+paint_estimate+carpet_estimate)
```

   Already you can see a lot of issues. For one thing we're not validating the inputs as numbers. Also there's a lot of weird repetition that makes this hard to read. Additionally this program only runs once then closes. Maybe we want to do a bunch of rooms. Maybe we want to save this so that we can open and change it later. For the remainder of the class we'll investigate these issues and try to improve on the above program.

## Functions: `def` and `return`

The above example doesn't actually do any error checking. If someone other than the author tried to use this they might input `twelve` instead of `12` or even `3'6"` instead of `3.5`. They will then receive a cryptic error that a non-programmer may not be able to understand. This means the line `height = raw_input("What is the height of the room?")` should be replaced with something like this:

```python
answer = False
while not answer:
    input = raw_input("What is the height of the room?")
    if input.isdigit():
        height = int(input)
        answer = True
    else:
        print "Invalid input. Please enter a number."
```

If you had to copy and paste these 8 lines over and over again your program would become very unreadable (pro-coders refer to this as "copy-pasta" or "spaghetti-code"). Additionally if you ever had to change this (let's say to allow `3'6"` as a valid input) then you would have to change multiple places, making the code difficult to maintain. What we really want is a new function `number = number_input(question)` that will execute the above code in a single line. Functions are defined using `def` (short for definition) and return a value using `return` (similar to print).

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
```

This is still 9 lines of code, but it can be re-used over and over again as a function. You can then substitute this for `raw_input` every where you want to insure that you get a number for the value:

```python
length = number_input("What is the length of the room?")
width = number_input("What is the width of the room?")
height = number_input("What is the height of the room?")
```

The basic syntax here is:

```python
def function_name(argument):
    # Do a bunch of stuff
    return some_value
```

And a few important notes

* The first line of a function looks similar to if statements and loops. They all start with a key word (in this case `def`) then have specific details (here the function name and arguments), and then end with a colon `:`. In all three cases you must use indentation to tell where the code begins and ends or you will get an `IndentationError`

* Function naming rules follow the same conventions as all variable names. In python we consider it better to use descriptive names rather than short, cryptic names.

* after `def` comes the function name followed by parentheses and then arguments. There can be zero to infinity arguments like so:

```python
def curse_zues():
    print "Zues, why have you forsaken me!!!"

def greet_user(name):
    print "Hello, "+name+". It is good to see you again."

def add3(number1,number2,number3):
    return number1 + number2 + number3
```

The above would work like this:

```python
>>> curse_zues()
Zues, why have you forsaken me!!!
>>> greet_user("Ditchy McAbandon Pants")
Hello, Ditchy McAbandon Pants. It is good to see you again.
>>> x = add(1,2,3)
>>> print x
6
```

Note that if a function receives fewer or greater arguments than is required, it will raise a `TypeError`. Also, `return`ing anything is actually optional. The first two functions printed but didn't return anything. 

* Lastly a function ends by returning a value. This is optional. Also you can put return in conditionals or forloops.

```python
def first_greater_than_5(some_list):
    for i in some_list:
        if i > 5:
             return i

my_list = [1,2,1,3,1,4,3,6,3,1,99,34,23,5,6,8]
print fist_greater_than_5(my_list) # prints 6
```

## Exercises

1. Write an `is_even(number)` function that returns `True` if a number is divisible by 2 and `False` if it is not.

2. For the super lazy, write an `is_odd(number)` function that uses the above function to tell if a number is NOT divisible by 2.

3. Write an `is_any_odd(some_list)` function that returns `True` if it finds any odd numbers in a list.

4. Write a `check_sum(some_string,digit)` function that does the following:

- cycle through a string, add all numbers (individual digits) in the string together. 

- ignore any non numeric numbers.

- `return True` if the last digit in the sum of all numbers is equal to the digit argument (hint: use `last_digit = my_sum%10`)

- Otherwise `return False`.
