l1=[]
l2=[]

l=["owl","lion","tiger","monkey","gemsbok"]
for i in l:
    l2.append(list(i))
for i in l2:
    i.sort()

n=int(input("enter the number of word you want to guess(limit 3-7):  "))
while True:
    if 2<n<8:
        break
    print("wrong choice of word length enter the number again")
    n=int(input(""))
     


turn=int(input("enter the number of trials u want(limit upto 15):  "))
while True:
    if n<=turn<16:
        break
    print("wrong choice of trials enter the number again")
    turn=int(input(""))
     

print("...............................lets begin the game....................................")
print("-------------------------------------------------------------------------------------------")


while turn>0:
    print("guess the char:  ")
    char=input("")
    l1.append(char)
    print(f"gussed words =={l1}")
    l1.sort()

    if set(l1)&set(l2[n-3])==set(l2[n-3]):
            print(f"you WON_______with efficiency {(n/len(l1))*100} and the guessed word is {l[n-3]} :  ")
            break
    turn=turn-1
    if turn==0:
        print("you loose:  ")