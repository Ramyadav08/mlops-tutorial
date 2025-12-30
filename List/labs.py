# remove duplicat from the list
L=[10,20,30,10,20,40,50,60,50,60]
L2=[]
for i in L:
    if i not in L2:
        L2.append(i)
print("List after removing duplicates:",L2)

print("***********************************")

# ask a number from user and check whether that number is present in the list or not if present print index else print not found
# num= int (input("Enter a number to search in the list:"))
# if num in L:
#     print("Number found at index:",L.index(num))
# else:
#     print("Number not found in the list")

# print("***********************************")

# reverse a list

# L3=[]
# L4=[]
# for i in range(0,6):
#     value= int (input("Enter value to add in the list:"))
#     L3.append(value)

# for j in range(len(L3)-1,-1,-1):
#     L4.append(L3[j])
# print("Original list:",L3)
# print("Reversed list:",L4)
    
# write a program to count occurrence of each element in the list and find highest occurrence element

L5=[10,20,10,30,20,10,40,50,30,20,10,20]

L6=[]

for i in L5:
    if i not in L6:
        L6.append(i)

hoc = 0          # highest occurrence count
hocelement = 0   # element with highest occurrence

shoc = 0         # second highest occurrence count
shocelement = 0  # element with second highest occurrence
for j in L6:
    c=L5.count(j)

    if c>hoc:
        shoc=hoc
        shocelement=hocelement
        hoc=c
        hocelement=j
    elif c>shoc and c!= hoc:
        shoc=c
        shocelement=j
    
    print("Element:",j,"occurs",c,"times")
print("\nHighest occurrence element:", hocelement, "occurs", hoc, "times")
print("Second highest occurrence element:", shocelement, "occurs", shoc, "times")


print("***********************************")
# two list and store only common elements in another list
L7=[10,20,30,40,50,60]
L8=[40,50,60,70,80,90]
L9=[]
for i in L7:
    if i in L8:
        if i not in L9:
            L9.append(i)
print("Common elements in both lists:",L9)








