
def char(char1,num,flag):
        l=[]
        pos1=0
        k=1
        for i in range(97,123):
                l.append(chr(i))
        
        for pos,i in enumerate(l):
                if i==char1:
                        pos1=pos1+pos
                        break
        while k<num+1:
                pos1+=1
                k=k+1
                if pos1>25:
                        pos1=0
        if flag==0:
                return l[pos1]
        else:
                return l[pos1].upper()





s=input()
n=int(input("enter the n0:"))
l1=list(s)
l3=[]
for pos1,i in enumerate(l1):
    if 96<ord(i)<123:
            l3.append(char(i,n,0))
    elif 64<ord(i)<91:
            l3.append(char(i.lower(),n,1))
    else:
            l3.append(i)
print(''.join(l3))       