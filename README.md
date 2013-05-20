Intro to Programming First Principles (May 2013)
========

1 - Instalation
--------

### Mac and Linux (unix based systems)

If you are using a Mac or Linux machine you most likely have python installed already. Pull up a terminal and type "python" and hit enter. If you see a line starting with ">>>" then you have python installed.

If not, follow the instructions in the next section.

### Windows

For this course we'll be using python 2.7, which can be downloaded from:

http://www.python.org/getit/

Select the installation package for your operating system. Be sure to get python 2.7.5 and not 3.3.2

2 - The python runtime
--------

Python can be run as scripts or entered directly into the python prompt. Enter into a python prompt (by typing 'python' into a terminal or by locating the "python shell" in IDLE). Then type `print "hello world"` and press enter. You should see the following:

```python
>>> print "hello world"
hello world
```

Now open a file by clicking `File >New Window` and then type `print "hello world"`.

Next execute the file by clicking `Run > Run Module`.

There is no difference between executing it line by line in the terminal and running a program.

3 - Basic Operations
--------

Python provides the following basic math operations:

\+ addition

\- subtraction

\* multiplication

\/ division (integer)

\% modulo division (remainder)

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

In order to understand a program, programmers will often write comments which are ignored by the computer. In python These are ignored by the computer and are only used to tell other programmers (or your future, forgetful self) what code means. In python comment lines are identified with a hash mark (#) and multi line strings are kept in triple quotes (""").

```python
"""
This line and the next one will not have any effect on the program.
After each of the following expressions I will put the answer in a comment.
"""

5 * (8-3)/4 # 6

1 * 2 * 3 * 4 * 6 * 7 * 8 # 8! or 40320

```
## 5 - Variables and expressions

Math is fun and all, but it would be hard to make a useful program with just numbers. Programs use variables to store and recall values. 

```python
>>> x = 1
