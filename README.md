Intro to Programming First Principles (May 2013)
========

## 0 - Introduction

### Why we program

* Humans make mistakes when repeating simple actions, computers do not (see also "free will vs determinism"). Computers also do these things much more quickly than we can.

* Smarter people have solved problems, computers give us access to those solutions.

* Once you write a program, you can pass it onto others (or your future self).

### Why python

* Very readable, very "human friendly".

* Batteries included (common problems are already solved in advance).

* Strong community (others solve problems so you don't have to).

* Object oriented, customizable.

## 1 - Installation

### Mac and Linux (unix based systems)

If you are using a Mac or Linux machine you most likely have python installed already. Pull up a terminal and type "python" and hit enter. If you see a line starting with ">>>" then you have python installed.

If not, follow the instructions in the next section.

### Windows

For this course we'll be using python 2.7, which can be downloaded from:

http://www.python.org/getit/

Select the installation package for your operating system. Be sure to get python 2.7.5 and not 3.3.2 because some of the course material herein will not work in the later version of python.

## 2 - The python runtime

Python can be run as scripts or entered directly into the python prompt. Enter into a python prompt (by typing 'python' into a terminal or by locating the "python shell" in IDLE). Then type `print "hello world"` and press enter. You should see the following:

```python
>>> print "hello world"
hello world
```

Now open a file by clicking `File >New Window` and then type `print "hello world"`.

Next execute the file by clicking `Run > Run Module`.

There is no difference between executing it line by line in the terminal and running a program.

## 3 - Basic Operations

Python provides the following basic math operations:

\+ addition

\- subtraction

\* multiplication

/ division (integer division, rounds down)

% modulo division (returns only remainder of integer division)

Test each of the above by typing a number then an operator then another number. Confirm that all of the following return 8.

```python
>>> 3 + 5

>>> 10 - 2

>>> 2 * 4

>>> 88 / 10

>>> 88 % 10
```

The last two may be a bit confusing. This is because 88 divided by ten gives 8 with a remainder of 8. In python division is "truncating", meaning that it only returns the integer part. So 88/10 gives 8 since 8*10 = 80. If you don't understand this, don't worry, it's not that important right now.

### Excercises

1. 6+4*10

2. (6+4)*10 (Compare this to #1, and note that Python uses parentheses just like you would in normal math to determine order of operations!)

3. Divide the numbers 1 through ten by 2 using integer division: `/`. Then divide the numbers 1 through 10 by 2 using modulo division `%`.

## 4 - Comments

In order to understand a program, programmers will often write comments which are ignored by the computer. In python These are ignored by the computer and are only used to tell other programmers (or your future, forgetful self) what code means. In python comment lines are identified with a hash mark (#) and multi line comments are kept in triple quotes (""").

```python
"""
This line and the next one will not have any effect on the program.
After each of the following expressions I will put the answer in a comment.
"""

5 * (8-3)/4 # 6

1 * 2 * 3 * 4 * 6 * 7 * 8 # 8! or 40320
```

## 5 - Variables and expressions

Math is fun and all, but it would be hard to make a useful program with just numbers. Programs use variables to store and recall values. Variables are basically names for values stored by the computer.

```python
>>> x = 1
>>> print x
1
>>> print x + 5 // doesn't change x!
6
>>> print x // see I told you
1
>>> x = x + 1
>>> print x
2
>>> y = x
>>> print y
2
>>> x = 100
>>> print y
2
```

This illustrates several important points.

* When you put a variable in an expression (e.g. `x + 1`) the variable doesn't change, but the result of the expression is returned.

* Variables can be assigned to expressions (e.g. `x = 1 + 1`) and the expressions can even contain the variable itself (e.g. `x = x + 1`).

* Once a variable is set equal to an expression, the expression is evaluated. Changing a variable in that expression does not change the first variable (specifically y does not change after we change the value of x). This is not true of all languages!

### Naming variables

`x` and `y` are great for mathematicians, but python is usually more "human friendly". Consider this word problem and the python solution:

```python
"""
Jim eats 3 cookies a day. If cookies come in packs of 20,
 how many packs (round down) does he eat in a year?
 How many cookies will he have left over at that time?
"""

cookies_per_day = 3
days = 365
cookies_per_pack = 20
cookies_per_year = cookies_per_day * days

# divide the number of cookies by the cookies in a pack to find out how many packs Jim eats
packs_per_year = cookies_per_year / cookies_per_pack

print packs_per_year

# the remainder is the modulo of cookies_per_year and cookies_per_pack
cookies_eaten_from_last_pack = cookies_per_year % cookies_per_pack

# subtract the cookies_eaten_from_last_pack and the cookies_per_pack
# this tells how many cookies are left in the pack
cookies_left_over = cookies_per_pack - cookies_eaten_from_last_pack

print cookies_left_over
```

The above code has very descriptive variable names and comments to explain the less intuitive calculations. Now what if you find out that Jim lives on the Neptune which has 60190 days in a year. All you have to do to correct the above program is change the number of days and re-run the program!

## Exercises

1. What is wrong with each of the following lines?

```python
my_birthday = 6/20/1983

my_dad = #1
```

2. If you drive 50 miles to work everyday (total) and your car gets 10 miles per gallon and gas costs $4 per gallon, how much gas do you use per week? Write a program to find this. Be sure to use descriptive variables so that when you get a new car you can recalculate this by only changing one value.

3. Try to solve this next one in your head before trying it on a computer. What is x equal to at the end of the following program?

```python
x = 2
y = 5
z = x * y
x = z - 1
y + 1
```

## Illegal names

Every programming language has rules for what you can and can't name a variable. The following are a list of rules and examples good and bad names:

* Names can contain letters, numbers and underscores, `_`. The following are all legal names: `count`, `x1`, `x2`, `day_2_awesomesauce`.

* Names cannot contain any other characters. The following are all ILLEGAL names: `day-three-milleage`, `james+julie`, `**fablous!!**`, `myspace.com`, `f%$^&_it`. These will usually generate SyntaxErrors.

* Names cannot start with numbers. This is an ILLEGAL name: `123go`

* Python has 29 keywords. For example, you can't name a variable `print` because that would prevent you from printing ever again. The following are all ILLEGAL names, because they would conflict with reserved python words:

```
and       def       exec      if        not       return
assert    del       finally   import    or        try
break     elif      for       in        pass      while
class     else      from      is        print     yield
continue  except    global    lambda    raise
```

## 6 - Strings

We have a long way to go before we get to useful programming. So far we have learned about integers, a numeric data type that can be used to perform mathematical operations. In this section we learn about three new types of data.

Try the following:

```python
name = "charlie"
name = 'daryl'
greeting = 'Hello ' + name
print greeting

time = "8:30"
print "I wake up at " + time + " everyday"

five_ones = '1'*5
print five ones
```

There are several important things here:

* With a few exceptions, a string can be any character wedged inbetween double or single quotes.

* Just like integers, strings can be set to variables and these variables can be overwritten.

* Strings can be added together. When you add two strings, they are "stuck together" to form a new string.

* Strings can be multiplied by integers. This is no different than repeatedly adding the string to itself multiple times.

Exercises:

1. Create a string with an apostrophe, such as: I can't figure out this problem

2. Create a string with both single and double quotes in the string. 

3. Try to figure out each of the following before typing them in

```python
'one plus one is ' + '1' + '1'

'Na na ' * 8 + 'batman!'

'I' + 'love' + 'bees'
```

## 7 - Error!

If you mistyped any of the examples up to this point, you may have seen something like the following:

```python
>>> '1' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

When python comes accross an error it prints out a traceback of everything it was doing at the time of an error. What's really important here is the last line: `TypeError: cannot concatenate 'str' and 'int' objects` this means that you tried to add a string and an int and rather than guessing what you meant, python decided to halt and inform you of the problem. Does '1' + 1 equal 2 or '11'? Some languages (javascript or php) guess what you mean and proceed without raising an error. This can lead to unpredictable results and difficult debugging. 

## 8 - A simple function: type()

Let's look more closely at the values used in the previous example:

```python
>>> print type(1)
<type 'int'>
>>> print type('1')
<type 'str'>
```

Here `type` is a function that returns the "type" of a value. Above we see two types, `int` and `str` which correspond to integers and strings. When you try to add an int to a str, python raises a `TypeError` telling you that two types were mixed incorrectly. We've actually seen a third type as we've done this. The third type is `type`.

```python
>>> print type(type)
<type 'type'>
```

But for now let's focus on the new use of parentheses. A function takes in zero or more variables and returns zero or more values like `output = function(variable_1,variable_2,...)`. In this case type converts a variable into it's corresponding "\<type>", or in python terms:

```python
type_of_x = type(x)
```

Similarly `int` and `str` can be used to convert a variable to an integer or string.

```python
int('1') + 1 # returns the number 2

'1' + str(1) # returns the string '11'
```

## 9 - `raw_input` and our first real program!

`raw_input` is a different type of function. It takes in a string and displays it to the user. The user then types in anything, and python returns a string of the users input.

```python
name = raw_input('What is your name? ')
age = raw_input('How old are you? ')
print "Hello " + name + ". You are " + age + " years old".
```

### Exercises

1. Modify the above program to tell a person how old they will be in 20 years.

2. Can you come up with an input for your program that causes an error? What is the difference between this error and the previous error?

## 10 - Lists and loops

Loops are at the heart of all programming languages. In python, loops cycle through a given set of values and run the same code repeatedly while changing one variable every time the loop repeats. Python uses indentation to determine what is inside a loop. The most basic loop in python looks like this:

```python
for variable in some_sequence:
    # do something with variable
```

Try the following:

```python
print "entering loop"
for letter in "ABCDEFG":
    print letter

print "exiting loop"
```

The output should look like this:

```
entering loop
A
B
C
D
E
F
G
exiting loop
```

As you can see, every time the loop repeats, the variable `letter` is assigned to the next letter in the string. You can change other variables inside the loop as well. Let's say you wanted to know which letter of the alphabet 'g' was. You could try something like this:

```python
number = 0
for letter in "ABCDEFG":
    print "Starting loop... number is "+str(number)
    number = number + 1

print "g is the " +str(number)+"th number in the alphabet"
```

Any variable can be can be changed inside the loop and when you exit the loop the change stays.

### Ninja exercise

1. Write a loop that prints your name.

Typically we do not iterate over a string but over a list. Lists are a series of any python object. For example, the following program counts to ten:

```python
for i in [1,2,3,4,5,6,7,8,9,10]:
    print i
```

A list is enclosed in brakets, `[]`, and the values of a list are separated by commas. Lists can hold any python value and even variables. Can you guess the output of this code?

```
x = 1
y = 'Susan'
for variable in [1,2,'monkey',x,y]:
    print variable
```

A very useful function in python is `range`. This takes in an integer and returns a list of the same length, starting with 0. The following code counts from 0 to 9.

```python
my_range = range(10)
print my_range
for i in my_range:
    print i
```

## Exercises

1. Write a program that will count to 100 by 5s (printing 0,5,10...100). There are many ways to solve this using what we've learned so far.

2. Save five names to a list. Print out the names. Then try to print the individual letters of each of the names (hint: you can put a loop inside a loop by indenting twice).

3. Range is very versitile in that it can take 1-3 arguments. Try each of the following. Can you deduce what range is doing with the extra arguments?

```python
print range(1,10)
print range(1,20)
print range(0,20,2)
print range(0,105,5)
```

## Contitionals

The final thing we need to start writting real programs is conditionals. Conditional statements block off code using indentation (much like loops). A conditional will only execute using if the conditional statement is evaluated as true. For example:

```python
if True:
    print "This will print"

if False:
    print "This will not print"
```

Here we introduce a new data type, the boolean. Booleans can either be `True` or `False`. If conditional is `True`, the code will execute, otherwise it will not.

Boolean operators compare two variables and are evaluated as `True` or `False`. 

```python
x = 1
y = 1
z = 2

# All of the following are `True`.
# read as "x is equal to 1"
x == 1

# x is equal to y
x == y

# x is not equal to z
x != z

# x plus one is equal to z
x + 1 == z

z == x + 1

y + 1 == z

# the type of x equals the type of z
type(x) == type(z)

x == int('1')

str(x) == '1'

# z is greater than x
z > x

# y is less than z
y < z

# x is less than or equal to y
x <= y

# z is greater than or equal to x
z >= x

# "not" reverses the value
not False

# works on variables and expressions
not x == 666
```

## Exercises

1. Write a program that asks a persons age (remember `raw_input`?). Then tell that person whether they are older, younger or the same age as you.

2. Wrap the previous problem in a for loop to makes sure that it gives the right answer for people age 0 to twice your age.

3. What does this program do? What is a better name for the variable `x`? Can you think of the limitations of this program? In otherwords, can you think of something you can type to give the "wrong" answer?

```python
x = ['Doug','Chris','Roland','Patrick','John']

user_name = raw_input("What is your name? ")
match = False
for name in x:
    if name == user_name:
        print "That's my brothers name!"
        match = True

if not match:
    print "Cool name, nice to meet you " user_name
```
