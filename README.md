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

* Powerful, sleek, and sexy (like a python).

## 1 - Instalation

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

/ division (integer)

% modulo division (remainder)

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
3. Divide the numbers 1 through ten by two using integer division: `/`. Then divide the numbers 1 through 10 by 2 using modulo division `%`.

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

* Variables can be assigned to expressions (e.g. `x = 1+1`) and the expressions can even contain the variable itself (e.g. `x = x + 1`).

* Once a variable is set equal to an expression, the expression is evaluated. Changing a variable in that expression does not change the first variable (specifically y does not change after we change the value of x).

### Naming variables

`x` and `y` are great for mathematicians, but python is usually more "human friendly". Consider this word problem and the python solution:

```python
"""
Jim eats 3 cookies a day. If cookies come in packs of 20, how many packs (round down) does he eat in a year? How many cookies will he have left over at that time?
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

## Illegal names

Every programming language has rules for what you can and can't name a variable. The following are a list of rules and examples good and bad names:

* Names can contain letters, numbers and underscores, `_`. The following are all legal names: `count`, `x1`, `x2`, `day_2_awesomesauce`.

* Names cannot contain any other characters. The following are all ILLEGAL names: `day-three-milleage`, `james+julie`, `**fablous!!**`, `myspace.com`, `f%$^&_it`. These will usually generate SyntaxErrors.

* Names cannot start with numbers. This is an ILLEGAL name: `123go`

* Python has 29 keywords. The following are all ILLEGAL names, because they would conflict with reserved python words:

```
and       def       exec      if        not       return 
assert    del       finally   import    or        try 
break     elif      for       in        pass      while 
class     else      from      is        print     yield 
continue  except    global    lambda    raise 
```
