set1=set()
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
s=input("")
for i in s:
    if i in lower_case:
        set1.add(1)
    if i in upper_case:
        set1.add(2)
    if i in special_characters:
        set1.add(3)
    if i in numbers:
        set
        set1.add(4)
# print(set1)
if len(s)>=6:
    num1=4-len(set1)
    print(num1)
if len(s)<4:
    print(6-len(s))
if len(s)>3 and len(s)<6:
    if len(set1)==1:
        print(3)
    if len(set1)==2:
        print(2)
    if len(set1)==3 or len(set1)==4:
        print(6-len(s))

