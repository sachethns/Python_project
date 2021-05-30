from tkinter import*
import random
cows=0
bulls=0
attempts=0
number=[]
root=Tk()
root.title("COWS AND BULLS")
root.state('zoomed')
canvas=Canvas(root,width=1600,height=1200,bg='light blue')
canvas.pack()
l1=Label(root,bg="grey",text="First Name:",fg="white",bd=5,font=("Times",12,'bold'))
canvas.create_window(800,100,window=l1)
e1=Entry(root,width=50)
canvas.create_window(800,200,window=e1)
l2=Label(root,bg="grey",text="Last name:",fg="white",bd=5,font=("Times",12,'bold'))
canvas.create_window(800,300,window=l2)
e2=Entry(root,width=50)
canvas.create_window(800,400,window=e2)
def click1():
    if len(e1.get())>0 and len(e2.get())>0:
        root=Tk()    
        root.title("COWS AND BULLS")
        root.state('zoomed')
        root.config(background='light salmon')
        l22=Label(root,text="Hi "+e1.get()+" "+e2.get(),bg="light salmon",fg="black",font=15)
        l22.pack()
        l6=Label(root,text="About the game:",fg="black",bg="light salmon",font=15)
        l6.pack()
        l7=Label(root,text="We generate a 4 digit number and you are supposed to guess it in 15 attempts!!\nYou get a COW for every correct digit in the correct place and a BULL for every correct digit in the wrong place.\nThe game ends when you get 4 cows and 0 bulls(that's when you guessed it right!).",fg="black",bg="light salmon",font=15)
        l7.pack()
        choice1=Label(root,text="Please enter a number with 4 DISTINCT DIGITS:",fg="black",bg="light salmon",font=15) 
        choice1.pack()
        choice=Entry(root,width=10)
        choice.pack()
        def MakeNumber():
            global number
            for i in range(4):
                x=random.randrange(0,10)
                number.append(x)
            if number[0]==0:
                number.clear()
                MakeNumber()
            if len(number)>len(set(number)):
                number.clear()
                MakeNumber()
        MakeNumber()
        def clicked():
            global number
            q=str(number[0])
            r=str(number[1])
            s=str(number[2])
            t=str(number[3])
            choice100=Label(root,text=q+r+s+t,font=12)
            choice100.pack()
            blnt=Label(root,text="Better Luck Next Time!!",font=("Helvetica",20,"bold"),bg="light salmon",fg="blue4")
            blnt.pack()
        def click():
            global cows
            global bulls
            global attempts
            global number
            if len(choice.get())>len(set(choice.get())):
                choice79=Label(root,text="Please enter a 4 digit number with distinct digits")
                choice79.pack()
                choice.delete(0,END)
            elif len(choice.get()) != 4:
                choice82=Label(root,text="Please enter a 4 digit number")
                choice82.pack()
                choice.delete(0,END)
            else:
                def PlayGame():
                    global cows
                    global bulls
                    global attempts
                    global number
                    m1=choice.get()
                    choice.delete(0,END)
                    attempts+=1
                    for i in range(4):
                        for j in range(4):
                            if(m1[i] != str(number[i])):
                                if i!=j:
                                    if(m1[i] == str(number[j])):
                                        bulls+=1
                    for x in range(4):
                        if m1[x] == str(number[x]):
                            cows+=1
                    if cows!=4 and attempts<=15:
                        m15="Cows: "+str(cows)+" Bulls: "+str(bulls)
                        l15=Label(root,text=m15,bg="light salmon",fg="black",font=12)
                        l15.pack()
                    elif attempts>15:
                        m18="You lost the game.Quit to know the number."
                        l18=Label(root,text=m18,bg="light salmon",fg="black",font=9)
                        l18.pack()
                    elif (cows == 4):
                        l17=Label(root,text="Cows : 4 Bulls : 0",bg="light salmon",fg="black",font=10)
                        l17.pack()
                        l16=Label(root,text="You win after "+str(attempts)+" attempts!",bg="light salmon",fg="blue4",font=("Helvetica",20,"bold"))
                        l16.pack()
                PlayGame()
                cows=0
                bulls=0
        b=Button(root,text="Lets start!",command=click,bg="light grey",fg="black",font=("bold",15))
        b.pack()
        bn=Button(root,text="Quit",command=clicked,bg="light grey",fg="black",font=15)
        bn.pack()
b1=Button(root,text="Click here to begin!",command=click1,bg="white",fg="midnight blue",font=("Helvetica",16,"bold"))
canvas.create_window(800,500,window=b1)
