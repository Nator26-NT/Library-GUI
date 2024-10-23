from tkinter import *
from tkinter import PhotoImage


root = Tk()
root.configure(bg='blue')

root.geometry("800x600")
root.title("Library")


title = Label(root, text="My Library" , font=('MS Sans Serif' , 20) , bg='white', fg='blue')
title.pack(padx= 10 , pady=10)

text = Text(height=1 , width= 50,bg="white" , fg='black')
text.pack(pady= 30, padx=100)

message = Label(root, text="|Search for any of your favorite Books|" ,  font=("Helvetica", 10) , bg="white", fg='black')
message.pack(pady=1)
btnroot  = Frame(root)
btnroot.pack()


btn1 = Button(btnroot,width=7, height=6  ,bg="red")
btn2 = Button(btnroot,width=7, height=6 ,bg="red")
btn3 = Button(btnroot,width=7, height=6 , bg="red")
btn4 = Button(btnroot,width=7, height=6 , bg="red")
btn5 = Button(btnroot,width=7, height=6 , bg="red")

btn6 = Button(btnroot,width=7, height=6 , bg="white")
btn7 = Button(btnroot,width=7, height=6 , bg="white")
btn8 = Button(btnroot,width=7, height=6 , bg="white")
btn9 = Button(btnroot, width=7, height=6 ,bg="white")
btn10 = Button(btnroot,width=7, height=6, bg="white")

btn11 = Button(btnroot,width=7, height=6, bg="black")
btn12= Button(btnroot,width=7, height=6, bg="black")
btn13= Button(btnroot,width=7, height=6, bg="black")
btn14= Button(btnroot, width=7, height=6, bg="black")
btn15 = Button(btnroot,width=7, height=6, bg="black")

btn1.grid(row=0 ,column=0)
btn2.grid(row=0 ,column=1)
btn3.grid(row=0 ,column=2)
btn4.grid(row=0 ,column=3)
btn5.grid(row=0 ,column=4)

btn6.grid(row=1 , column=0)
btn7.grid(row=1 , column=1)
btn8.grid(row=1 , column=2)
btn9.grid(row=1 , column=3)
btn10.grid(row=1 , column=4)

btn11.grid(row=2, column=0)
btn12.grid(row=2, column=1)
btn13.grid(row=2, column=2)
btn14.grid(row=2, column=3)
btn15.grid(row=2, column=4)

Pbtnroot = Frame(root)
Pbtnroot.pack()
Pbtn1 = Button(Pbtnroot,width=1, height=1 , bg="white" , text="1")
Pbtn2 = Button(Pbtnroot,width=1, height=1 , bg="white" , text="2")
Pbtn3 = Button(Pbtnroot,width=1, height=1, bg="white" , text="3")
Pbtn4 = Button(Pbtnroot, width=1, height=1 ,bg="white" , text="4")
Pbtn5 = Button(Pbtnroot,width=1, height=1, bg="white" , text="5")

Pbtn6 = Button(Pbtnroot,width=1, height=1, bg="white" , text="6")
Pbtn7= Button(Pbtnroot,width=1, height=1, bg="white", text="7")
Pbtn8= Button(Pbtnroot,width=1, height=1, bg="white" , text="8")
Pbtn9= Button(Pbtnroot, width=1, height=1, bg="white" , text="9")
Pbtn10 = Button(Pbtnroot,width=1, height=1, bg="white" , text="10")
Pbtn12 = Button(Pbtnroot,width=1, height=1, bg="white" , text=">>nk")


Pbtn1.grid(row=5, column=0)
Pbtn2.grid(row=5, column=1)
Pbtn3.grid(row=5, column=2)
Pbtn4.grid(row=5, column=3)
Pbtn5.grid(row=5, column=4)


Pbtn6.grid(row=5, column=5)
Pbtn7.grid(row=5, column=6)
Pbtn8.grid(row=5, column=7)
Pbtn9.grid(row=5, column=8)
Pbtn10.grid(row=5, column=9)


root.mainloop()