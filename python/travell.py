l=[
    ['JFK', 'ATL', 150],
    ['ATL', 'SFO', 400],
    ['ORD', 'LAX', 200],
    ['LAX', 'DFW', 80],
    ['JFK', 'HKG', 800],
    ['ATL', 'ORD', 90],
    ['JFK', 'LAX', 500],
    ['SFO','AAA',100],
    ['CCC','AAA',300],
    ['ATL','CCC',100]
    
]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
s=0
source=input("enter the source: ")
dest=input("enter the destination: ")


for i in l:
   if source==i[0] and dest==i[1]:
       l1.append(i)
# print(l1)


for i in l:
    if source==i[0]:
        l2.append(i)
for i in l:
    if dest==i[1]:
        l3.append(i)
for i in l2:
    for j in l3:
        if i[1]==j[0]:
            l4.append(i)
            l4.append(j)
# print(l4)


for i in l2:
    for j in l3:
        for k in l:
            if i[1]==k[0] and j[0]==k[1]:
                l5.append(i)
                l5.append(k)
                l5.append(j)
# print(l5)


d1=dict()
for i in l1:
    k=i.pop()
    d1[tuple(i)]=k
# print(d1)


d2=dict()
for i in range(0,len(l4),2):
    s=l4[i][-1]+l4[i+1][-1]
    d2[(l4[i][0],l4[i][1],l4[i+1][1])]=s
# print(d2)


d3=dict()
for i in range(0,len(l5),3):
    s=l5[i][-1]+l5[i+1][-1]+l5[i+2][-1]
    d3[(l5[i][0],l5[i][1],l5[i+2][0],l5[i+2][1])]=s
# print(d3)
l11=[]
for i in d1.values():
    l11.append(i)
l11.sort()
if len(l11)!=0:
    n1=l11[0]
else:
    n1=100000

l12=[]
for i in d2.values():
    l12.append(i)
l12.sort()
if len(l12)!=0:
    n2=l12[0]
else:
    n2=10000

l13=[]
for i in d3.values():
    l13.append(i)
l13.sort()
if len(l13)!=0:
    n3=l13[0]
else:
    n3=10000

if n1<n2 and n1<n3:
    print(f"{list(d1.keys())[list(d1.values()).index(n1)]} is {n1}")

elif n2<n1 and n2<n3:
    print(f"{list(d2.keys())[list(d2.values()).index(n2)]} is {n2}")

elif n3<n1 and n3<n2:
    print(f"{list(d3.keys())[list(d3.values()).index(n3)]} id {n3}")





    










    
        



    
    


