class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        return self.num**2
    def cube(self):
        return self.num**3
    def root(self):
        return self.num**0.5
num=int(input("Enter a number: "))
calc=Calculator(num)
print(f"The square of {num} is {calc.square()}")
print(f"The cube of {num} is {calc.cube()}")
print(f"The square root of {num} is {calc.root()}")
