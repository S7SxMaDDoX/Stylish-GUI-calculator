from tkinter import*
import tkinter
from PIL import Image, ImageTk

a=Tk()
a.title("GAURU")
a.geometry("355x533")
a.resizable(0,0)

# Set the window icon
#a.iconphoto(True,icon)
def calculate(event=None):
    expression = value.get()
    try:
        result = str(eval(expression))
        value.set(result)
    except Exception as e:
        value.set("Error")

a.bind('<Return>', calculate)

#evaluation of expression
def gau(event):
    global value
    text =event.widget.cget("text")
    print(text)
    
    if text == "=":
        if value.get().isdigit():
            value = int(value.get())
        else:
            soln = eval(b.get())
            print(soln)
            value.set(soln)
            b.update()
    elif text == "c":
        value.set("")
        b.update()
    elif text == "⌫":  # Backspace button
        current_value = value.get()
        if current_value:
            new_value = current_value[:-1]
            value.set(new_value)
            b.update()
#print value in entry box 
    else:
         value.set(value.get()+ text)
         b.update()

#clear logic 
#def clear():
 #   global value
  #  value.set(" ")
 

#entry logic         
value=StringVar()
value.set("")
ammu=Frame(a,background='deepskyblue',borderwidth=6)
b=Entry(ammu,textvar=value,justify=RIGHT,font=('arial', 18, 'bold'),foreground="deepskyblue",bg="white")
b.grid(row=0,columnspan=4,ipadx=170,ipady=29)
b.pack(ipady=25,ipadx=40) 
ammu.grid(row=0,columnspan=4)



# buttons of calcultor 
y=Button(a,text="7",bd=8,bg="deepskyblue",fg="black")
y.grid(row=1,column=0,ipadx=29,ipady=25,columnspan=1)
y.bind("<Button-1>",gau)
z=Button(a,text="8",bd=8,bg="deepskyblue",fg="black")
z.grid(row=1,column=1,ipadx=29,ipady=25,columnspan=1)
z.bind("<Button-1>",gau)
c=Button(a,text="9",bg="deepskyblue",bd=8,fg="black")
c.grid(row=1,column=2,ipadx=29,ipady=25)
c.bind("<Button-1>",gau)
d=Button(a,text="4",bg="deepskyblue",bd=8,fg="black")
d.grid(row=2,column=0,ipadx=29,ipady=25)
d.bind("<Button-1>",gau)
e=Button(a,text="5",bd=8,bg="deepskyblue",fg="black")
e.grid(row=2,column=1,ipadx=29,ipady=25)
e.bind("<Button-1>",gau)
f=Button(a,text="6",bg="deepskyblue",bd=8,fg="black")
f.grid(row=2,column=2,ipadx=29,ipady=25)
f.bind("<Button-1>",gau)
g=Button(a,text="1",bg="deepskyblue",bd=8,fg="black")
g.grid(row=3,column=0,ipadx=29,ipady=25)
g.bind("<Button-1>",gau)
h=Button(a,text="2",bd=8,bg="deepskyblue",fg="black")
h.grid(row=3,column=1,ipadx=29,ipady=25)
h.bind("<Button-1>",gau)
i=Button(a,text="3",bg="deepskyblue",bd=8,fg="black")
i.grid(row=3,column=2,ipadx=29,ipady=25)
i.bind("<Button-1>",gau)
j=Button(a,text="00",bg="deepskyblue",bd=8,fg="black")
j.grid(row=4,column=0,ipadx=25,ipady=25)
j.bind("<Button-1>",gau)
k=Button(a,text="0",bd=8,bg="deepskyblue",fg="black")
k.grid(row=4,column=1,ipadx=30,ipady=25)
k.bind("<Button-1>",gau)
l=Button(a,text=".",bg="deepskyblue",bd=8,fg="black")
l.grid(row=4,column=2,ipadx=30,ipady=25)
l.bind("<Button-1>",gau)
m=Button(a,text="*",bd=8,bg="deepskyblue",fg="black")
m.grid(row=1,column=3,ipadx=29,ipady=25)
m.bind("<Button-1>",gau)
n=Button(a,text="/",bd=8,bg="deepskyblue",fg="black")
n.grid(row=2,column=3,ipadx=29,ipady=25)
n.bind("<Button-1>",gau)
o=Button(a,text="-",bd=8,bg="deepskyblue",fg="black")
o.grid(row=3,column=3,ipadx=29,ipady=25)
o.bind("<Button-1>",gau)
p=Button(a,text="+",bd=8,bg="deepskyblue",fg="black")
p.grid(row=4,column=3,ipadx=29,ipady=25)
p.bind("<Button-1>",gau)
q=Button(a,text="c",bg="deepskyblue",bd=8,fg="black")
q.grid(row=5,column=0,ipadx=28,ipady=25)
q.bind("<Button-1>",gau)
r=Button(a,text="%",bd=8,bg="deepskyblue",fg="black")
r.grid(row=5,column=1,ipadx=28,ipady=25)
r.bind("<Button-1>",gau)
s=Button(a,text="⌫",bd=8,bg="deepskyblue",fg="black")
s.grid(row=5,column=2,ipadx=24,ipady=25)
s.bind("<Button-1>",gau)
t=Button(a,text="=",bd=8,bg="lightskyblue")
t.grid(row=5,column=3,ipadx=29,ipady=25)
t.bind("<Button-1>",calculate)



#to hold screen
a.mainloop()
