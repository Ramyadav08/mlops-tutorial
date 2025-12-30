#when function call itself

def ten_to_one(n):
    if n < 1:
        return
    print(n)
    ten_to_one(n - 1)
ten_to_one(10)

print("---------------------")
def one_to_ten(n):
    if n > 10:
        return
    print(n)
    one_to_ten(n + 1)
one_to_ten(1)

print("---------------------")

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))  

print("---------------------")

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))


print("---------------------")

def sum_of_n(n):
    if n<=0:
        return 0
    return n + sum_of_n(n-1)
print(sum_of_n(5))