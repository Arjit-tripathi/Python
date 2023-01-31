Assignment - 5 Full Stack Web Development using Python MySirG
Operators
1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)

num=int(input("Enter a number"))
remove_last_digit=num
print(remove_last_digit//10)


2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

num=int(input("Enter a number"))
last_digit=num
print(last_digit%10)

3. Write a python script to swap data of two variables

a=int(input ("Enter value A : "))
b=int(input("Enter value B : "))
a,b=b,a
print("value of a",a)
print("value of b",b)

4. Write a python script to find x power y, where values of x and y are given by user
x=int(input("Enter the value: "))
y=int(input("Enter the power: "))
power=x**y
print("Power is=",power,"user enter the value: ",x,"user enter the power",y, sep='\n')


5. Write a python script which takes a three digit number from the user and displays
only its first digit.
num=int(input("Enter a three digit number: "))
first_digit=num
print(first_digit//100)


6. Write a python script which takes a three digit number from the user and displays
only its middle digit.
number=int(input("Enter a three digit number: "))
number=int(number/10)
answer=(number%10)
print(answer)


7. Write a python script which takes a three digit number from the user and displays
only its last digit.
num=int(input("Enter a number"))
last_digit=num
print(last_digit%10)

8. Write a python script to use IN operator to display the data present in the list
list1=[90.3,29,0,20,30,40,50]
print(20 in list1)

9. Write a python script to use NOT IN operator to display the data not present in list
list2=90.3,29,0,20,30,40,50
200 not in list2
print(200 not in list2)

10. Write a python script to use IS operator to display if both variables are the same
object or not?
a=5     
b=5
c=6

print(a is b)
True
      
print(a is not c )    
True

print(a is not b)      
False


