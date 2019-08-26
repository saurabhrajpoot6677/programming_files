s1=input("")
n=int(input(""))
list1=[]
for i in range(0,n):
    n1=int(input(""))
    list1.append(n1)
s=s1+"$"
l=[]
flag=0
add=0
for i in range(0,len(s)-1):
    if s[i]!=s[i+1]:
        l.append(ord(s[i])-96)
        add=0
        flag=0
    if s[i]==s[i+1]:
        if flag==0:
            add=(ord(s[i])-96)+(ord(s[i])-96)
            flag=1
            l.append(add)
        else:
            add=add+(ord(s[i])-96)
            l.append(add)
l1=list(set(l))
print(l1)
for i in list1:
    if i in l1:
        print("Yes")
    else:
        print("No")