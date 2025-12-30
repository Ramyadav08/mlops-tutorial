L=[1,2,3,4,5,6,7,8,9,10]

mid = len(L)//2
L1=L[:mid]
L2=L[mid:]
print("First half of the list is:",L1)
print("Second half of the list is:",L2)

print("***********************************")

# swapping the first enlement with last element of the list

L[0],L[-1]=L[-1],L[0]
print("List after swapping first and last element is:",L)