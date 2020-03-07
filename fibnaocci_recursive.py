# Function for nth Fibonacci number

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


num = int(input("enter a number between 0 and 30 :\n"))

if num < 0 or num > 30:
    print("wrong entry")
else:
    print(Fibonacci(num))
