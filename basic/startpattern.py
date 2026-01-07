n=6
#rectangle
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

print("***********************************")

#inc triangle

for i in range(n):
    for j in range(0,i):
        print("*",end=" ")
    print()

print("***********************************")
# dec triangle
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

print("***********************************")

# right side inc triangle
for i in range(n):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
print("***********************************")

# right side dec triangle
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(5,i,-1):
        print("*",end=" ")
    print()

print("***********************************")

# pyramid
for i in range(n):
    for j in range(5,i,-1):
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
    for j in range(5,i,-1):
        print("* ",end="")
    for j in range(4,i,-1):
        print("* ",end="")
    print()

print("***********************************")

# # diamond
# for i in range(n):
#     for j in range(i,n)



print("***********************************")
