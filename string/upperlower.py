name="RamRekha Yadav"
result=""
for i in name:
    ch= ord(i)
    if ch>=97 and ch<=122:
        result=result+chr(ch-32)
    else:
        result=result+chr(ch)
print("String after converting lowercase to uppercase:",result)


#lowercase

lowers=""
for i in name:
    ch=ord(i)
    if ch>=65 and ch<=90:
        lowers=lowers+chr(ch+32)
    else:
        lowers=lowers+chr(ch)
print("String after converting uppercase to lowercase:",lowers)

# uper to lower and lower to upper using swapcase() function

result1=""
for i in name:
    ch = ord(i)
    if ch >=65 and ch<=90:
        result1=result1+chr(ch+32)
    elif ch>=97 and ch<=122:
        result1=result1+chr(ch-32)
    else:
        result1=result1+chr(ch)
