## Find the largest element in a list
L=[20,10,40,30,50,90,5,7,60]

Max=L[0]
for i in range(len(L)):
    if L[i]>Max:
        Max=L[i]
print("Largest element in the list is:",Max)


# Find the smallest element in a list

Min=L[0]
for i in range(len(L)):
    if L[i]<Min:
        Min=L[i]
print("Smallest element in the list is:",Min)


# Find the second largest element in a list
lagrest=secondLargest=float('-inf')
for i in range(len(L)):
    if L[i]> lagrest:
        secondLargest=lagrest
        lagrest=L[i]
    elif L[i]> secondLargest and L[i]!= lagrest:
        secondLargest=L[i]
print("Second largest element in the list is:",secondLargest)

# Find the second smallest element in a list
smallest=secondSmallest=float('inf')
for i in range(len(L)):
    if L[i]<smallest:
        secondSmallest=smallest
        smallest=L[i]
    elif L[i]<secondSmallest and L[i]!=smallest:
        secondSmallest=L[i]
print("Second smallest element in the list is:",secondSmallest)
