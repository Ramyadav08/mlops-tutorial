n=int(input("Enter number: "))
flag=False
if n>=2:
    for i in range(2,n//2+1):
        if n%i==0:
            flag=True
            print("this is not prime number")
            break
    if flag==False:
        print(n,"is prime number")
    
        
    
