n=12345
res=0
while True:
    rem=n%10
    res=res+rem
    n=n//10
    if n==0:
        break
print("Sum of digits is:",res)