s=input()
l=['S','O','S']
l1=[]
count=0
for i in range(0,len(s)-2,3):
    l1.append([s[i],s[i+1],s[i+2]])
print(l1)
for k in l1:
    m=0
    for j in k:
        if j!=l[m]:
            count=count+1
            m=m+1
        else:
            m=m+1

        
print(count)


