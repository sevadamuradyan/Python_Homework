# Recursion variant
def f(n):
    if n < 0:
        return "Wrong Input!"
    else:
        if n < 3:
            return n
        return f(n - 1) + f(n - 2) + f(n - 3)


print(f(7))


# Loop variant
def fib_3(n):
    a = 0
    b = 1
    c = 2
    while n > 0:
        a, b, c = b, c, a + b + c
        n -= 1
    return a


print(fib_3(7))


# Tail recourse
def fib_3p(n, a=0, b=1, c=2):
    return a if n == 0 else fib_3p(n - 1, b, c, a + b + c)


print(fib_3p(7))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def pas(n, m):
    if m < 0 or n < m:
        return "Wrong Input!"
    return fact(n) / (fact(m) * fact(n - m))


print(pas(3, 2))
