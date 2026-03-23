# Tutedude-Assignment-2
ASSIGNMENT TASK-1 (CHECK IF A NUMBER IS EVEN  OR ODD)
PROGRAM:
#Python program to check the given number is even or odd
number=input("Enter an integer: ")    
if number.isnumeric():
    if int(number)%2==0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
else:
    print(f"{number} is not a number") 
    
WORKING:
First we read the input dynamically from the user by using intput() function into a variable named (number)
After that in the conditional statement of (if) it checks the first condition
In the condition it is number.isnumeric() function which is of general syntax variable_name.isnumeric() is a built in function which checks for only numbers.
It returns TRUE if the variable contains all numbers only.
In the inner (if) we have converted inputed number into integer type and performed remainder division with 2 which gives remainder as the result.
If it is true that means read number is an even as for even number 2 is perfectly divisible, so inside the (if) a print statement is written.
In the else part if (number)%2 is not equals to 0 ( (number)%2!=0) then the read number is an odd number, hence a print statement is written.

 EXAMPLE:1
 Enter an integer: 7
 7 is an odd number

 EXAMPLE:2
 Enter an integer: 16
 16 is an even number

ASSIGNMENT TASK-2  (SUM OF INTEGERS FROM 1 TO 50)
PROGRAM:
#Python program to perform Sum of Integers from 1 to 50 Using a Loop
n=int(input('Enter your n value:'))
total_sum=0
for i in range(1,n+1):
    total_sum+=i
print(f'The sum of numbers from 1 to {n} is:',total_sum)

WORKING:
Here first we read integer input dynamically from the user by using int(input()) function and store it in the variable named n.Here we use n for general purpose
Next we initialized a variable named total_sum to 0.
In the for loop which is from the range (1 to n+1) here we used n for general purpose,
In the for loop total_sum=total_sum+i , now here for first iteration i=1 and total_sum=0 so total_sum+=i will be 1+0=1, which again gets stored in total_sum.
In the second iteration i=2 and total_sum=1 hence total_sum+=i will be 2+1=3 , which will gets stored in total_sum.
In the similar process the loop runs upto n times as the provided range is (1,n+1).
At last outside of the loop in the print statement we print the total_sum as the result.

EXAMPLE:1
Enter your n value:50
The sum of numbers from 1 to 50 is: 1275

EXAMPLE:2
Enter your n value:97
The sum of numbers from 1 to 97 is: 4753

