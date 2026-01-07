n=153
res=0
tem=n
while True:
    rem=tem%10
    res=res+(rem**3)
    tem=tem//10
    if tem==0:
        break
if res==n:
    print(n,"is an Armstrong number")
else:   
    print(n,"is not an Armstrong number")