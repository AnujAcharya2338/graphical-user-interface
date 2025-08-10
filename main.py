# import tkinter

# window= tkinter.Tk()
# window.title("WOW")
# window.minsize(width=500,height=300)
        
# label=tkinter.Label(text="I am inevitable")
# label.pack(side="left")

# def add(*args):
#     s=0
#     for n in args:
#          s += n
#     return s

# def calculate(n,**kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2,add=3, multiply=5)
# print(add(3,4,5,6))   
        
# window.mainloop()


from tkinter import *


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"


input = Entry(width=20)
input.pack()


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    


button = Button(text="CLick", command=button_clicked)
button.pack()


window.mainloop()