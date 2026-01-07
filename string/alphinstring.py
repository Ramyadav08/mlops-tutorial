# count the alphabets in a given string

name="Ramrekha09 Yadav!!"
count=0
for i in name:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        count+=1
print("The number of alphabets in the given string is:",count)

u=0
l=0
for i in name:
    if i>='a' and i<='z':
        l=l+1
    elif i>='A' and i<='Z':
        u=u+1   
print("The number of uppercase letters is:",u)
print("The number of lowercase letters is:",l)