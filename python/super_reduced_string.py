s=input("")
l=list(s)
l.append("#")
l.append("#")
i=0
flag=0
while True:
    if l[i]==l[i+1] and l[i]!="#":
        l.pop(i)
        l.pop(i)
        i=0
    elif l[i]!=l[i+1] and l[i+1]!="#":
        i=i+1
    elif l[i+1]=="#":
        break
l.pop()
l.pop()
# print(l)
if len(l)==0:
    print("Empty String")
else:
    print(''.join(l))
