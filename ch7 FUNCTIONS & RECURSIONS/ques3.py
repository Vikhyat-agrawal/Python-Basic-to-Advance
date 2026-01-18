def sum(n):
    sum=0
    if n>0:
        sum=sum+n+sum(n-1) 
    return sum
num=int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {num} is {sum(num)}")