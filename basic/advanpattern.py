n=6

#inc ttri
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

print("***********************************")

# dec tri
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()

print("***********************************")

# right side inc tri

for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

print("***********************************")

# right side dec tri

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

print("***********************************")

# pyramid
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i):
        print("* ",end="")
    for j in range(i-1):
        print("* ",end="")
    print()

print("***********************************")

# reverse pyramid
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("* ",end="")
    for j in range(i+1,n-1):
        print("* ",end="")
    print()

print("***********************************")
# diamond

for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i):
        print("* ",end="")
    for j in range(i-1):
        print("* ",end="")
    print()
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for k in range(i,n-1):
        print("* ",end="")
    for k in range(i+1,n-1):
        print("* ",end="")
    print()

print("***********************************")

#vertical pyramid
for i in range(n-1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()

print("***********************************")
# rev vertical pyramid

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

print("***********************************")

#horizontal nepal flag
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
