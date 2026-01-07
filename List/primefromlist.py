L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
L1=[]
for i in L:
    flag=False
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                flag=True
                break
        if flag==False:
            L1.append(i)
           
print("Prime numbers from the list are:",L1)