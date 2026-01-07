n= 23452
res=0
while True:
    rem= n%10
    res=(res*10)+rem
    n=n//10
    if n==0:
        break
print("Reversed number is:",res)

