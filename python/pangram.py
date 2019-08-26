s=input("")
s1=s.lower()
l=[]
l1=[]
for i in s1:
    if 96<ord(i)<123:
        l.append(i)
for i in l:
    if i not in l1:
        l1.append(i)
if len(l1)==26:
    print("pangram")
else:
    print("not pangram")