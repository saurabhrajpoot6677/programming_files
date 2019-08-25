import random
print("()",end="      ")
for i in range(99,0,-1):
    if i%10!=0:
        if i<10:
            print(f"0{i}",end="      ")
        else:
            if i==14 or i==24 or i==34 or i==48 or i==58 or i==68 or i==72 or i==82 or i==92:
                i="||"
                print(i,end="      ")
            elif i==53 or i==33 or i==49 or i==29 or i==97 or i==77:
                i="))"
                print(i,end="      ")
            elif i==87 or i==39 or i == 43:
                i="(("
                print(i,end="      ")
            else:
            
                print(i,end="      ")
    else:
        print("")
        print(i,end="      ")
print("")
print(".............................................................................")
print(".............................................................................")

sum1=0
sum2=0
while True:
    player1=int(input("player one chance press 1: "))
    if player1==1:
        num1=random.randint(1,6)
    player2=int(input("player two chance press 2: "))
    if player2==2:
        num2=random.randint(1,6)
    sum1=sum1+num1
    print(f"player one is at {sum1}")
    sum2=sum2+num2
    print(f"player two is at {sum2}")
    if sum1==100:
        print("player one won: ")
        break
    if sum2==100:
        print("player two won")
        break
    if sum1==14 or sum1==48 or sum1==72:
        sum1=sum1+20 
        print(f"player one is at {sum1}")
    if sum2==14 or sum2==48 or sum2==72:
        sum2=sum2+20
        print(f"player two is at {sum2}")

    if sum1==29 or sum1==33 or sum1==77:
        sum1=sum1-20
        print(f"player one is at {sum1}")
    if sum2==29 or sum2==33 or sum2==77:
        sum2=sum2-20
        print(f"player two  is at {sum2}")
    if sum1>100:
        sum1=sum1-num1
    if sum2>100:
        sum2=sum2-num2

    



    