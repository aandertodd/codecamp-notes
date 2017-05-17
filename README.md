# CodeCamp Notes

Lesson notes for LaunchCode's Immersive CodeCamp

*Week One*

##Binary:
Binary is base2 (2 numbers before starting over at 0)

0, 1
counting..
0 = 0, 1 = 1, 10 = 2

##Hexadecimal:
Hexadecimal is base16 (16 numbers and letters before starting over at 0)

represents numbers using
0, 1, 2, … 9, a, b, c, d, e, f

a = 10
b = 11
c = 12…

16 = 1 * 16^1 + 0 * 16^0 = #10
17 = 1 * 16^1 + 1 * 16^0 = #11
18 = 1 * 16^1 + 2 * 16^0 = #12

# represents hex number

33 = 2 * 16^1 + 1 * 16^0 = #21

228

2 * 16^2 + 2 * 16^1 * 8 * 16 ^ 0


#Environment variable

PATH - locations of runnable programs

Shell is a specific command line interface/program
BASH is a shell (unix)
shell uses forward slash (/c/user) where \ is normally used
when at a command prompt you are always at a specific location
you can find that by typing pwd

drwxr-xr-x
d on far left of l list stands for directory
next three (rwx) are user
next three (r-r) are group
next three (r-x) everybody

Permissions:
r = read
w = write
x = execute

Commands:

ls shows everything in folder (not hidden)
ls -a shows (a stands for all) hidden files as well
ls -l (l stands for long listing)
chmod u+x
touch myfile
cd .. (up or back one directory)
mkdir (make directory)
mv (move)
~ (home directory)
rm (deletes and DOES NOT ask permission)
rm -rf (force remove)
sudo rm -rf / (will delete everything in the system. DON’T DO)
man (manual pages/documents about commands)

Absolute path - the definitive location for a file and is the same no  matter where you are
			  in the prompt (always starts with /) user/dev/launchcode
Relative path -  relative to where you are right now
			  (folder you are in and where you are looking) dev/launchcode

Day 4

Version Control = keep different versions of the same file(s) as a history
Why?
revert changes if we break things
different versions of the same project
“you have no history”
enable collaboration — big deal for programmers

git init — initializes empty git repository for the folder you name (stores data elsewhere)
README.md — creates a file that says hey look heres info about this
git add README.md (add or “staging” your changes)
git status — tells you whats going on right now (%50 of what you will use in git)
git commit -m (tells the repository to keep a copy of the file)
git add . (stage ALL changes)
git log — shows history of the file
git diff — shows difference between current stage and what has already been committed
new changes aren’t stored to the file until you commit

git hub (is NOT git) is a website where we can put git repositories
1. link repositories between your pc and and git hub
2. push/pull (no difference between a push or pull)

git remote add origin <location>
git remote -v — will show if your repository is linked between pc and internet

pull is a fetch + merge
fetch “hey i wanna look at that” merge “put that with my code too”

git push origin master
git pull origin master

status, add, commit, push (main uses in git)

Day 5

*see markdown practice.rtf

HTML - Hypertext Markup Language
markdown (is a markup language) used on the web
use browser to view “renders” html

CSS - cascading stylesheets (controls the visual appearance of almost every web page)

Every html file should have a doc type that determines which version of html the page is
written in.
HTML is nested.
Indent for each level of nesting
Should always have a head and a body element

***the HTML you write should have NOTHING to do with visual styles***
CSS will do this for us.
Why?
1. separation of concerns
2. our pages are not always read by humans

We should practice semantic HTML (meaning and syntax)

HTML5 doctor. Describes all HTML elements relevant to HTML5

3 places for CSS
1. inline - attached to a HTML element
2. document level (usually in the <head> and with <style> tags)
3. Separate file (stylesheet) .css

these rules cascade that’s why it’s called cascade

Selectors:
element selector  = h1{
ID selector = #heading{ (more specific)
class selector = .blue{ (on a heading, paragraph, link, anything you want to change)

*Week Two*

##Algorithm
is a self-contained step-by-step set of operations to be performed (to solve a problem, carry out operation)

##Syntax 
defined by formal rules, does not specify meaning
Semantics does

## Value Error
when a function is expecting a certain type of parameter and you send it another type instead.


## Name Error
almost always means using a variable before it has been assigned a value (uisng an identifier that hasn't been created yet).

Example: print(my_value)

## Parse Error
is a type of syntax error. Usually means you left out punctuation, paren, etc.

Example: print("hello)

## Type Error
happens when you try to combine items that are incompatible (attempting to carry out an operation with incompatible type(s)).

## Syntax Error
there is a line of code that python doesn't know what to do with (missing colon, indent, etc.).

## Semantic Error
doesn't give you the outcome you want (logic error).

## Attribute Error
caused by using an object attribute that is not defined.

## Indentation Error
Not following Python's whitespace rules.

How to avoid bugs:
Work in small units*
using good names for things (semantics)*



SUBMIT HOMEWORK:
run report from unit-1-assignment-sleepytodd1
./generate-report.sh (generates report)
git status
git commit -m "comment"
git push origin master
your repository link plus /report.html (grade report)
(stage, commit, push. every single time.)

##Loop Components
1.The task that should be repeated
2.The data set that should be used with the task

##Lists
[value1, value2, value3,...]
value is a data, a string, etc.

a list is a single value but with multiple values inside of it.
most programming languages won't let you mix str with int, but python does.

how to check if it's a List:
value = [1, 2, 3, 4]
print(type(value))

##For Loops
A for loop allows us to repeat a section of code a specific number of times by using a list.
the list is the loop body (defines the loop)*
the loop ends when you stop indenting following lines
the loop also ends when the list has been exhausted

##Range function
print(range(5))

output:[0, 1, 2, 3, 4]
starts counting at 0

to create more custom/complicated lists, use:
range(start, stop, step)
start - the first number in the list
stop - the last number in the list + 1
step - how you count to that number

count to 100
range(1, 101, 1)

count to 100 evenly
range(0, 101, 2)

countdown*
range(100, -1, -2)

##Turtles
Turtle is a module that will let us build simple images using loops.

import turtle <<< tells python we are using turtle graphics
zach = turtle.Turtle() <<< Names and creates turtle
zach.forward(50) <<< distance and direction

using a variable

side_length = 50
zach.forward(side_length)
zach.left(90)
zach.forward(side_length)
zach.left(90)
zach.forward(side_length)
zach.left(90)
zach.forward(side_length)

DRY* Don't Repeat Yourself
there's a cleaner way to write this with less chance for error

import turtle
zach = turtle.Turtle()

side_length = input("How long should the square's sides be?")

for side in range(4):
    zach.forward(side_length)
    zach.left(90)

to find what shape you're making divide number of sides by 360 degrees***

##Brief introduction of functions
print, input, range are a few
print("hello world")
name = input("What's your name")
some_numbers = range(1,15, 2)

In these examples the parameters are:
"hello world"
"what's your name?"
(1, 15, 2)

what you get in exchange for these functions you get a value called a RETURN VALUE

we can write our own functions!
def *must start the line* followed by your function name which defines the entry point for the function
following line must be indented because it belongs to that function

ex:
def hello_world():
    return "Hello world"
message = hello_world()
print(message)

output is hello world; the empty parens mean no parameter

ex:
def hello_world(name):
    return "Hello " + name

message = hello_world("Sally")
print(message)

##Modules
ex: turtle
It's a collection of python code that is bundled up for others to use, but which is not part of the core python programming language.
To use modules, we must install and then import them.

There are only 3 modules available: turtle, math, random.

installing a module requires a program like pip or conda.
$ conda install pytest
$ pip install pytest-html

pip - installs packages from the Python Package Index, viewable at pypi.org
conda - installs packages from the Anaconda repository

import to use modules, always put them at the top.
the identifier (turtle) is now available for us to use within our file.

import random
random.random() - returns a random float between 0 and 1
random.randomrange(n, m) - returns a random integer between n and m-1

**random is pseudo-random which is not actually random, but random based off of a previous number**

generate a random float between 1 and 5
num = random.random()
num = num*4 [that gives you a random number between 0 and 4]
num = num+1 [shifts number over 1 making it now between 1 and 4]
+ is a shift and * is a stretch in this scenario

##Running python in terminal
type python press return
>>> means that you are no longer in a normal terminal shell

###Turtle in class Studio
import turtle
import random
#create two Turtles
zach = turtle.Turtle()
jesse = turtle.Turtle()
zach.color("blue")
jesse.color("orange")
zach.shape("turtle")
jesse.shape("circle")
*forward(units)
left(angle)
one random step - turn random, go forward random*
#loop, taking random steps each time
for steps in range(5):
*(0, 360) int
pick number between 1 and 50*
#get random angle
    zach_angle = random.randrange(0, 360)
    jesse_angle = random.randrange(0, 360)

#get random distance#move by those amounts
    zach_dist = random.randrange(1, 50)
    jesse_dist = random.randrange(1, 50)
#move by those distances
    zach_forward(zach_dist)
    zach_left(zach_angle)
    jesse_forward(jesse_dist)
    jesse_forward(jesse_angle)

##function
 is a named sequence of statements that carry out a specific task.
 (nice packaging of an Algorithm)

 calling a function means running the function in a code with return values

 Visualizing a function:
 parameter(s) >> function >> return value (no matter how many parameters you only get one return)

 creating a function for something allows you to reuse that code anywhere in the program
 if you don't store a return variable/value it goes away

 *Activity*

 Function composition is putting a function in a function
 ex: age = int(input("What's your age?"))

if you put code after a return statement it doesn't execute
or the function "exits" when a return statement runs

*Some More Questions

1. Does a function have to have parameters - no, a function may have zero or more parameters, as decided by the programmer.
2. What happens if we call a function without providing a value for one of more input parameters? We get a type error
3. Does a function have to have a return value? no
4. What happens if we have a function that doesn't have a return value, but we try to store a result in a variable? the value that is implicitly returned and stored is the **special value**

the default return of a funtion without a result is none

##Scope
all variables and parameters within a program have a scope. Their scope determines how they may be accessed and used.

ex:
def add_two(num):
 	num = num+2
    return num + 2 (using this elminates the need for the temporary num variable)
add_two(2)
print(num)

input parameter or variable only exist within the function

##Local scope
variables and parameters within a function have local scope. They may only be accessed within the function in which they are defined. We call these variables local variables.

##Global scope
variables and parameters that are not defined within a function have global scope. They may be accessed from anywhere within the given file or program.

num = 2 << Global
def print_num(): << local
	print(num)

print_num()

functions can see things outside of themselves but can't pull from other functions

##Shadowing

num = 2

def print_num(num):
	print(num)

print_num(3)

*this situation has two variables with the same name. in this case, the new variable inside the box (local) ignores (or shadows) the global variable. You also can't change the global variable inside of a local function.*

*To find the absolute value of a number use 
print(abs(put number here))

*math module has a pow function
print(math.pow(number, power))

*max returns the max number sent to it
works with lists and can take any number of args separated by ,
print(max(7, 11))  prints 11

##Accumulator Pattern
def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)

This process of breaking a problem into smaller subproblems is called functional decomposition.

non fruiful function (or procedure) doesn't return a value 
------------

##Making decisions
*Branching*

code block << true << condition >> false >> code block #2

programs make decisions in the form of true or false (Boolean) *another type* (other types: str, int, float, list)
-must be capitalized
-are not strings; True is different from "True"
-are the result of certain arithmetic comparison expressions

    print(type(True))

    Output: <class 'bool'>

Comparisons: > < >= <= == != 
comparisons turn into a true or false

##Boolean Algebra

Ex: It is Friday and we are in class (and says both are true)
Ex: I am either asleep or awayke (or says one or the other is true)

##Boolean order of OPERATIONS

**
* / // %
+ -
comparisons


##Conditional Syntax (Branching in action)
starts with if condition:
    the next line (code block 1) is indented
ends with else:
    second block of code is also indented

Ex:
if expression_or_variable:
    code
else:
    code 2

% 2 == 0 (shows number is even) same as saying n % 2 == 0
% 2 == 1 (shows number is odd) same as saying n % 2 == 1
% 3 == 0 (shows number is multiple of 3, can be done with any number)

Else conditional is optional

##Nesting Conditionals
if n < 0 :
    print("n is negative")
else: 
    if n > 0:
        print("n is positive")
    else:
        print("n is is 0")

##The elif Clause
we can have multiple branches -- that is, multiple tests -- within the same conditional using elif

if n < 0:
    print("n is negative")
elif n > 0:
    print("n is positive")
else:
    print("n is 0")

*Conditionals only print the first statement it comes across that is True (even if several statements are True)!!*

##radius of circle example:

import math <<< (module example)

def calculate_area_of_circle(radius): <<< (function example, functionn should contain the algorithm)
    area = math.pi(since we imported math) * radius**2
    return area

radius = float(input("What is the radius of your circle?")) <<< test code


if radius >= 0:
    area = calculate_area_of_circle
    print("The area of a circle of radius", radius, "is", area)
esle:
    print("You gave a negative radius. That doesn't work, try again.")

##Simple spell-checker example:
#given a word, determine if it is spelled correctly
def is_spelled_correctly(word): <<< the name of the function tells you this will be a boolean return
    dictionary = ["launchcode", "coding", "blue", "rocket"]
    #return a boolean
    for term in dictionary:
        if word == term:
            return True
    
    return False
print(is_spelled_correctly("red"))

-----------
Week 3

##While Loop
 "indefinite"

while condition:

 code block

 boolean expression
 -comparison
 -boolean function
 -variable or value

 loop as long as condition is true
 danger in the fact that it might never be false
 if the condition is false we will have an infinite loop

ex of infinite loop:
while(True):
    print(i)
    i += 

where infinite loops might be useful:
-games (often infinite)
-web server

while(true):
    # respond to requests

How to ask quesions:
-clearly state what my problem is (where you're confused)
-clearly state what you do understand
-clearly state what you have tried (what did you try and why didn't it work)
-where have you looked for information?

data types - int, str, bool, lists, float

##Primitive Data Types
can it be broken down into something smaller? 
primitive can't be broken down - int, float, bool
not collections

##Composite or Non-primitive
can be broken down - lists and strings (dog "d" "o" "g", [0,1,2,3] 0 1 2 3)
collections

#Characters
we'll refer to a string of length 1 as a character
many programming languages have their own character data type, but Python does not

#Empty collections
we can have collection without anything in the collection [] ''

#Ordered collecions
lists and strings are ordered collections and have a specific order.
we refer to the place of an individual item in that order as it's *index*.
we may acces the individual components using the index of that item.

#Brack notation
allows us to get an individual item out of a list or string
for a list my_list we can get the item with index i using: my_list[i]

***ex:
message = 'Hello'
print(message[1])

output: e (because e is the letter at index 1)***

*strings behave like lists of characters*

***
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphabet)): # range(26) -> [0, 1, 2, 3... 25]  DONT DO THIS (maybe sometimes you can, reversing a string, printing every other character from a string)
    print(alphabet[i]) 

for letter in alphabet: DO THIS / MUCH BETTER TO READ AND IS SIMPLER
    print(letter)
***

user_string = input("Enter a string: ")
new_str = ''

for letter in user_string:
    if letter != 'a':
        new_str = new_str + letter
print(new_str)

True of "strings as lists":

ordered collection
indexes/bracket notation
loops over string

Not true of "strings as lists"
name = "chris"
name[0] = 9
[0, 'a', True] (lists can be mixed types and strings can not!)

##Good Problem Solving tips:
- pay attention to implicit information
- writing things down
- asked questions
- thinking through different possibilities

Problem solving is
intuitive
creative
practiceable
synthetic
hard
rewarding
a process

Problem solving is NOT
formulaic
repetitive
easy

#Principles
DONT panic
restate the problem (in your head, in writing, to a classmate)
outline the problem (write down what you know, subdivide into steps)
reduce the problem (think about a simpler version of the problem)
look for similarities (have you solved something similar before, how are they sim/diff?)
DONT panic
