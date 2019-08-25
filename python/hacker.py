def func(s):
    l=list("hackerrank")
    m=0
    for i in range(0,len(s)):
        if s[i]==l[m]:
            m=m+1
            if m==len(l):
                break

    if m==len(l):
        print("YES")
    else:
        print("NO")
         
n=int(input(""))
for i in range(0,n):
    s=input("")
    func(s)

