def addnumbers(n):
    res=0
    while True:
        rem=n%10
        res+=rem
        n=n//10
        if n==0:
            break
    print("Sum of digits is:",res)

addnumbers(12345)

print("-------------------------------------------")

def revnumber(n):
    res=0
    while True:
        rem=n%10
        res=(res*10)+rem
        n=n//10
        if n==0:
            break
    print("Reversed number is:",res)
revnumber(123452)

print("-------------------------------------------")

def armstrong(n):
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
armstrong(153)

print("-------------------------------------------")

def armstrongrange(n1,n2):
    for i in range(n1,n2+1):
        res=0
        tem=i
        while True:
            rem=tem%10
            res=res+(rem**3)
            tem=tem//10
            if tem==0:
                break
        if res==i:
            print(i,end=" ")
armstrongrange(1,1000)

print("\n-------------------------------------------")

def primeNumber(n):
    flag=False
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                flag=True
                print(n,"is not a prime number")
                break
        if flag==False:
            print(n,"is a prime number")
primeNumber(29)


print("-------------------------------------------")

def primeInRange(n1,n2):
    for i in range(n1,n2+1):
        flag=False
        if i>1:
            for j in range(2,(i//2)+1):
                if i%j==0:
                    flag=True
                    break
            if flag==False:
                print(i,end=" ")
primeInRange(1,50)


print("\n-------------------------------------------")

def factorial(n):
    res=1
    while True:
        res=res*n
        n=n-1
        if n==0:
            break           
    print("Factorial is:",res)
factorial(5)


def word_frequency(filepath):
    try:
        word_count={}
        with open(filepath, "r") as file:
            for line in file:
                words=line.split()
                for word in words:
                    word=word.lower().strip(".,!?\"';:()[]{}")  
                    if word in word_count:
                        word_count[word]+=1
                    else:
                        word_count[word]=1
        return word_count
    except FileNotFoundError:
        return "File not found."
    
print(word_frequency("sample.txt"))

"""
word=word.lower().strip(".,!?\"';:()[]{}")  
word.lower() converts the word to lowercase (so The and the are treated the same).
.strip(".,!?\"';:()[]{}") removes any of those punctuation characters from the start or end of the word (so word, becomes word, "(hello)" becomes hello).
"""