#the zero game: 21 coins
#Shereen Hassan 20170130
#Two players game

p1=0
p2=0
n=21
while (n>=1):
    p1=int(input("Player one play"))
    while(p1< 1 or p1 >3) :
        print ("wrong input,please re-enter within range")
        p1=int(input("Player one play"))
    if (p1 >= 1 and p1 <= 3):
        n=n-p1
    print("n =",n)
    if(n==1):
        print("Player one wins!")
        break
    p2=int(input("Player two play"))
    while(p2< 1 or p2 >3) :
        print ("wrong input,please re-enter within range")
        p2=int(input("Player two play"))
    if(p2>=1 and p2<=3):
        n=n-p2
    if(n==1):
        print("Player two wins!")
        break

    print("n =",n)
