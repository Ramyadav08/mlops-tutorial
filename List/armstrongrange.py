L=[i for i in range(1,1001)]
armstrong_numbers=[]

for j in L:
    res=0
    tem=j
    while True:
        rem=tem%10
        res=res+(rem**3)
        tem=tem//10
        if tem==0:
            break
    if res==j:
        armstrong_numbers.append(j)
print("Armstrong numbers between 1 and 1000 are:",armstrong_numbers)