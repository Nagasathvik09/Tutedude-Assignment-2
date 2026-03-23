#Python program to perform Sum of Integers from 1 to 50 Using a Loop
n=int(input('Enter your n value:'))
total_sum=0
for i in range(1,n+1):
    total_sum+=i
print(f'The sum of numbers from 1 to {n} is:',total_sum)

