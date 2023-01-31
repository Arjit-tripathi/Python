Assignment - 7 Full Stack Web Development using Python MySirG
Match Case
1. Write a python script to display the number of days in a given month number.

month=int(input("Enter the number : "))
match month:
    case 1:
        print("January")
    case 2:
        print("February") 
    case 3:
        print("March")       
    case 4:
        print("April")
    case 5:
        print("May")    
    case 6:
        print("june")    
    case 7:
        print("july")    
    case 8:
        print("August")    
    case 9:
        print("September")    
    case 10:
        print("Octuber")    
    case 11:
        print("November")    
    case 12:
        print("December")   
    case _:
        print("Please correct enter the months number")  


2nd==>using tupple
month= int(input("Enter a month number"))
match month:
    case month if month in(1,3,5,7,8,10,12):
        print("31 days")
    case month if month in (4,6,9,11):
        print("30 days")
    case 2:
        print("28 days or 29 days")
    case _:
        print("Invalid month")


2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
print("1. Addition")
print("2. subtraction")
print("3. multiplication")
print("4. Division")
print("Enter your choice")
choice=int(input())
match choice:
    case 1:
        print("Enter two no")
        a,b=int(input()),int(input())
        c=a+b
        print("sum is :",c)
    case 2:
        print("Enter two no")
        a,b=int(input()),int(input())
        c=a-b
        print("Subtraction is :",c)
    case 3:
        print("Enter two no")
        a,b=int(input()),int(input())
        c=a*b
        print("Multiplication is :",c)
    case 4:
        print("Enter two no")
        a,b=int(input()),int(input())
        c=a/b
        print("Division is :",c) 
        
3. Write a menu driven program with the following options:
    
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.


print("1. lengths of an isosceles triangle or not")
print("2. lengths of sides of a right angled triangle or not")
print("3. numbers are equilateral triangle or not")
print("4. Exit")
print("Enter your choice")
choice=int(input())
match choice:
    case 1:
        print("Enter three no")
        a,b,d=int(input()),int(input()),int(input())
        c=a=d
        print("isosceles triangle or not is :",c)
    case 2:
        print("Enter three no")
        a,b,d=int(input()),int(input()),int(input())
        c=a=b=d
        print("equilateral triangle or not is :",c)
    case 3:
        print("Enter three no")
        a,b,d=int(input()),int(input()),int(input())
        c=a<b<d
        print("right angled triangle or not is :",c)
    case 4:
        exit()
    
4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.

age=int(input("Enter a age"))
match age:
    case age if age<10:
        print("Kids")
    case age if age<20 :
        print("Teen")   
    case age if age<40:
        print("young")
    case age if age<60:
        print("Experienced")
    case age if age>=60:
        print ("Senior Citizen")  



5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.

no=int(input("Enter a number: "))
match no:
    case no if no%2==0:
        print("Saurabh Shukla")    
    case no if no<0:
        print("Prateek Jain")    
    case no if no>0 :
        print("Aditya Choudhary")  

6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement

s=input("Enter a string")
s.strip()
match s:
    case s if ' ' in s:
        print("Multi words string")
    case s if ' 'not in s:
        print("Single word string")

7. Write a python program to check whether a given number is positive, negative or
zero using match case statement

no=int(input("Enter a number: "))
match no:
    case no if no>0:
        print("Positive")
    case no if no<0:
        print("Negative")
    case no if no==0:
        print("Zero")  

8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement

s1=input("Enter a fist string: ")
s2=input("Enter a second string: ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("identical string")
    case (s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s2,s1))

9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year

10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday

s1=input("What is your favrotie color")
l1=["yellow","Blue","Orange","White","Black","Red"]
for colour in l1:
    if colour in s1:
        c=colour
        break
    else:
        c="other"
    
match c:
    case "yello":
        print("Monday")
    case "Blue":
        print("Tuesday")
    case "Orange":
        print("Wednesday")
    case "White":
        print("Thursday")
    case "Black":
        print("Friday")
    case "Red":
        print("Saturday")
    case "other":
        print("Sunday")
    



        





