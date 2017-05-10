# CodeCamp Notes

Lesson notes for LaunchCode's Immersive CodeCamp

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
