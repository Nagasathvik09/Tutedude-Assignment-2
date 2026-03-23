#Python program to check the given number is even or odd
number=input("Enter an integer: ")
if number.isnumeric():
    if int(number)%2==0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
else:
    print(f"{number} is not a number")

