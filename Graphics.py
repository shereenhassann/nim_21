from tkinter import*
game=Tk()
frame=Frame(game)
frame.pack()
    
background = PhotoImage( file = "Untitled-2.png"  )
lab = Label( frame , image = background )
lab.pack()

welcome=Label(frame,text="Welcome to 21 coins game!", bg="Pink", fg="White")
welcome.pack()
welcome.place( x = 350,y = 20)

def oneplayer():
    l1=Label(frame, text="It's your turn", bg="Pink", fg="White")
    l2=Label(frame, text ="Play:")
    l1.pack(side=TOP)
    l2.pack(side=LEFT)

    e1= Entry(frame, bd=4)
    e1.pack()
    e1.place(x=100, y=30,width=50, height=25)
    oneplayer.config(text="Play:")
    e2=Entry(frame, bd=4)
    e2.pack()
    e2.place(x=100, y=60, width=50, height=25)

    e2.delete(0,END)
    submit.pack()
    submit.place(x=700, y= 500)


def twoplayers():
    
    
    e2=Entry(frame, bd=4)
    e2.pack()
    e2.place(x=100, y=60, width=50, height=25)
    submit.pack()
    submit.place(x=700, y= 500)
    
    twoplayers.config(text="Player two:")
    oneplayer.config(text="Player one:")
    
    
oneplayer = Button(frame,text="One player", bg="Pink", fg="White",bd=4, command= oneplayer)
oneplayer.pack()
oneplayer.place(x=15, y=30)
twoplayers = Button(frame,text="Two players", bg="Pink", fg="White",bd=4, command= twoplayers)
twoplayers.pack()
twoplayers.place(x=15, y=60)

def submit():

    n=21
    p1=v.get
    print(p1)
submit = Button(frame, text="Submit",fg="blue", bd=4, bg="White",command=submit)











game.mainloop()
