L=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(L)-1,-1,-1):  # iterating through index of list in reverse order
    print(L[i],end=" ")

print("\n***********************************")

# all even number present in the list

for i in L:   # iterating through elements of list
    if i%2==0:
        print(i,end=" ")

print("\n***********************************")

for i in range(len(L)):  # iterating through index of list
    if L[i]%2!=0:
        print(L[i],end=" ")

print("\n***********************************")

# sum of all list elements
sum=0
for i in L:
    sum+=i
print("Sum of all elements in the list is:",sum)

print("***********************************")

# maximum element in the list
L1=[-10,-20,-3,-4,-5]
max=L1[0]
for i in range(0,len(L1)):
    if L1[i]> max:
        max=L1[i]
print("Maximum element in the list is:",max)
   
print("***********************************")

# minimum element in the list
min=L1[0]
for i in range(0,len(L1)):
    if L1[i]< min:
        min=L1[i]
print("Minimum element in the list is:",min)

print("***********************************")

# second largest element in the list

L2=[10,20,4,45,99,67,89,34,98]
max2=L2[0]
for i in range(0,len(L2)):
    if L2[i]> max2:
        max2=L2[i] 
    

print("Maximum element in the list is:",max2)

# append will add the value at the end of the list
# insert will add the value at the specified index (index,value)
# update will update the index value like a[0]=100
# pop by default pop will remove the last element of the list
# pop(index) will remove the element at the specified index
# remove will remove the specified value from the list
# clear will remove all the elements from the list
# del will delete the list permanently and also help to delete the specified index value   

#in set pop will remove first element of the set as set is unordered collection of elements