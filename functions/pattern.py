# inc tri

def inc_tri(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        print()

inc_tri(6)
print("********************************")
    
# dec tri

def dec_tri(n):
    for i in range(n):
        for j in range(i,n-1,):
            print("*",end=" ")
        print()

dec_tri(6)

print("********************************")

# rigth tri

def right_tri(n):
    for i in range(n):
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
right_tri(6)

print("********************************")

def right_dec_tri(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        print()
right_dec_tri(6)

print("********************************")

# pyramid
def pyramid(n):
    for i in range(n):
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i*2+1):
            print("*",end=" ")
        print()
pyramid(6)

print("********************************")

def rev_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i+1,n-1):
            print("*",end=" ")
        print()
rev_pyramid(7)
   
print("********************************")

def diamond(n):
    for i in range(n-1):
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i-1):
            print("*",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(n-1):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i+1,n-1):
            print("*",end=" ")
        print()
diamond(7)

print("********************************")

def left_full_tri(n):
    for i in range(n-1):
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i,n-1):
            print("*",end=" ")
        print()
left_full_tri(6)

print("********************************")

def right_full_tri(n):
    for i in range(n-1):
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        print()
right_full_tri(6)

print("********************************")

def half_left_right(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()

half_left_right(6) 
print("********************************")

def full_left_right(n):
    for i in range(n-1):
        for j in range(i):
            print("*",end=" ")
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i,n-1):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        for j in range(i):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        print()
  

full_left_right(6)