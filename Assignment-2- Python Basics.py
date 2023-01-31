Assignment-2: Python Basics
1. Write a python script to add comments and print “Learning Python” on screen.
#"Learning Python"

2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
'''
a=10
b='arjit'
c=3+4j
d="testing"
'''
3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print(type(a),type(b),type(c),type(d),type(e), sep="\n")
print()

4. Write a python script to print the id of two variables containing the same integer values.

var1=4
var2=4
print(id(var1))
print(id(var2))
print()      

5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable

val1=90
val2="MysirG"
val3=False
val4=2.89
print(type(val1),type(val2),type(val3),type(val4), sep="\n")
print()
print(id(val1),id(val2),id(val3),id(val4), sep="\n")
print()


6. Write a python script to print all the keywords

step1: import keyword
step2: print(keyword.kwlist)

7. On Python shell use help() function and display the list of keywords

step1: help()
step2: keywords

8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py

#A1.py
x=5

#A0.py
import A1
print(A1.x)

9. Name the keywords, used as data in the Python script.

True,False,None

10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format
(like: 13-8-2022 and 9:00 PM)

from datetime import datetime
x=date.today()
d1=x.strftime("%d-%m-%Y and %I:%M %P")
print("Today date:",d1)


