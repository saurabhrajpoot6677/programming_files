from itertools import combinations
s=input()
l=list(s)
l1=[]
main=[]
maxi=0
for i in l:
        if i not in l1:
                l1.append(i)
# print(l1)
l2=[]
l3=[]
n=len(l1)
n1=n-2
list1=[]
if len(l1)>2:
        comb = list(combinations(l1, n1))
        # print(comb)
if len(l1)>2:
        for i in comb:
                l2=l.copy()
                for j in i:
                        while j in l2:
                                l2.remove(j)
                l3.append(l2)

        for i in l3:
                count1=0
                for j in range(0,len(i)-1):
                        if i[j]==i[j+1]:
                                count1=count1+1
                if count1==0:
                        main.append(i)
        for i in main:
                list1.append(len(i))
        if len(list1)>0:
                maxi=max(list1)
        else:
                maxi=0


if len(l1)==2:
        count=0
        for i in range(0,len(l)-1):
                if l[i]==l[i+1]:
                        count=count+1
        if count>0:
                maxi=0
        else:
                maxi=len(l)
if len(l1)<1:
        maxi=0

print(maxi)       


