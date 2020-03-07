def fibonacci(n: int) -> int:
    xn2 = 0
    xn1 = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            xn = xn1 + xn2
            xn2 = xn1
            xn1 = xn

        return xn

num = int(input("enter a number :\n"))
if num < 0:
    print("incorrect answer")
else:
    print(fibonacci(num))
