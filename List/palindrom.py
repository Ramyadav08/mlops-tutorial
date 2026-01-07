n=121
tem=n 
res=0
while True:
    rem=tem%10
    res=(res*10)+rem
    tem=tem//10
    if tem==0:
        break
if res==n:
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")



