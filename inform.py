from tkinter import*
from tkinter import messagebox
import tkinter import ttk

def inform():

    inform = Tk()
    inform.geometry('590x550')
    inform.title("BMIW")
    inform.configure(background='#660000')
    inform.resizable(width=False,height=False)

    header = PhotoImage(file = "You Inform.png")

    Label(inform, image=header, borderwidth=0).grid(row=1, column=0)
    Label(inform, text="Your Weight"+"      "*6,font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=2,column=0)

    weight = Entry(inform,font="consolas 14", bg="#FFFFFF",fg="#660000")
    weight.grid(row=3,column=0)

    kg = ttk.Combobox(inform,values = ['Kilogram','Pound'],font="Mali 8", state = "readonly", width=20)
    kg.grid(row=3, column=0,sticky='E' )
    kg.set("Choose one....")

    Label(inform, text="Your Height"+"      "*6,font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=5,column=0)

    height = Entry(inform,font="consolas 14", bg="#FFFFFF",fg="#660000")
    height.grid(row=6,column=0)

    hi = ttk.Combobox(inform,values = ['Kilogram','Pound'],font="Mali 8",state = "readonly", width=20,)
    hi.grid(row=6, column=0, sticky='E')
    hi.set("Choose one....")

    weight1 = weight.get()
    height1 = height.get()

    Label(inform, text='\n',font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=8,column=0)

        def main():
        noti = messagebox.askyesno("Check!",'Save this information?')
        if True:
            pass
            ###ใส่พวก check
        else:
                noti.destroyed()

    submit = Button(inform, text="Submit",bg="#FFFFFF",fg="#660000",font ="consolas 10",command=main).grid(row=8,column=0)
    down = PhotoImage(file="ploo.png")

    Label(inform, image=down,borderwidth=0).grid(row=9,column=0)
    inform.mainloop()

inform()
