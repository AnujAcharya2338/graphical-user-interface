from tkinter import *
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

def button_clicked():
    output_text=input.get()
    mile_text= round(float(output_text) * 1.60934)
    output.config(text=mile_text)
    


my_label1 = Label(text=" Miles ")
my_label1.grid(column=2,row=0)

my_label2 = Label(text=" is equal to ")
my_label2.grid(column=0,row=1)

output = Label(text="0")
output.grid(column=1,row=1)

km =Label(text="Km")
km.grid(column=2,row=1)

input = Entry(width=10)
input.grid(row=0,column=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()