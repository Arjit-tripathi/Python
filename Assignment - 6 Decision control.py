Assignment - 6 Full Stack Web Development using Python MySirG
Decision Control
1. Write a python script to check whether a given number is positive or non-positive
#single line if else
print("Postive" if int(input("Enter a no")) >0 else "non postive")

#if-else
a=int(input ("Enter aNumber : "))
if a>0:
    print("Number is postive")
else:
    print("Number is NonPostive")
        

2. Write a python script to check whether a given number is divisible by 5 or not
#if-else
a=int(input ("Enter a Number : "))
if a%5==0:
    print("Number is divisible by 5")
else:
    print("Number is Not divisible by 5")

#single line if else
print("Number is divisible by 5" if int(input("Enter a no")) %5==0 else "Number is not divisible by 5")
    

3. Write a python script to check whether a given number is even or odd
#single line if else
print("even" if int(input("Enter a number: ")) %2==0 else "odd")

4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
a=int(input("Enter a Number A: "))
b=int(input("Enter a Number B: "))
if a>b:
    print("A is Greater")
else:
    print("B is Greater") 

5. Write a python script to print two given words in dictionary order
print("Enter two word")
a,b=input(),input()
print(b,a) if a>b else (a,b)
   

6. Write a python script to check whether a given number is a three digit number or not.
a=int(input("Enter a Number "))
if 99<a<1000:
    print("three digit no")
else:
    print("not a three digit no")


7. Write a python script to check whether a given number is positive, negative or zero.
a=int(input("Enter a Number "))
if a>0:
    print("postive")
elif a<0:
    print("Negative")
else:
    print("Zero")
    
    

8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
print("Enter value of a,b andc of quardic equation")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("real and distinct root")
elif d==0:
    print("Real and equal")
else:
    print("imagenary roots")

9. Write a python script to check whether a given year is a leap year or not.
print("Enter a year no")
year=int(input())
if year%400==0 or year%100!=0 and year%4==0:
    print("Leep year")
else:
    print("non leap year")
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
print("Enter three no")
a,b,c=int(input()),int(input()),int(input())
print((a if a>c else c)if a>b else(b if b>c else c))
   

11. Write a python script to take the month value in numeric format and display the
number of days in it.

month=int(input("Enter month no"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28 or 29 days")
else:
    print("invalid month no")
    

12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part

x=complex(input("Enter a complex no")
print(x.real)if x.real>x.imag else print(x.imag)
