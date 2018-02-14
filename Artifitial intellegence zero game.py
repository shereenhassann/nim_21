#the zero game: 21 coins
#Shereen Hassan 20170130
#AI game
n=21

while (n<=21):
    

    p1=int(input("Your turn, play:"))
    while (p1<1 or p1>3):
        print("Wrong number, choose between 1 and 3")
        p1=int(input("Your turn, play:"))
    if (p1>=1 and p1<=3):
        n=n-p1
        print ("n =",n)
    if (n==1):
        print("You WIN!")
        break
    
    if (n==5):
        n=n-1
    elif(n==6):
        n=n-2
    elif(n==7):
        n=n-3
    elif(n==2):
        n=n-1
    elif(n==3):
        n=n-2
    else:
        n=n-2
    if(n==1):
        print("You LOSE!")
        break
    
    print ("Computer played","n =",n)


    

