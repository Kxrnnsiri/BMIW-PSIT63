from tkinter import*
from tkinter import messagebox
from tkinter import ttk

def inform():

    inform = Tk()
    inform.geometry('590x430')
    inform.title("BMIW")
    inform.configure(background='#660000')
    inform.resizable(width=False,height=False)

    header = PhotoImage(file = "You Inform.png")

    Label(inform, image=header, borderwidth=0).grid(row=1, column=0)
    Label(inform, text="Enter Your Weight:"+"       "*6,font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=3,column=0)

    weight = Entry(inform,font="consolas 14", bg="#FFFFFF",fg="#660000")
    weight.grid(row=4,column=0)

    kg = ttk.Combobox(inform,values = ['Kilogram','Pound'],font="Mali 8", state = "readonly", width=20)
    kg.grid(row=4, column=0,sticky='E' )
    kg.set("units..")

    Label(inform, text="Enter Your Height:"+"       "*6,font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=6,column=0)

    height = Entry(inform,font="consolas 14", bg="#FFFFFF",fg="#660000")
    height.grid(row=8,column=0)

    unit = ttk.Combobox(inform,values = ['meter','cm'],font="Mali 8",state = "readonly", width=20,)
    unit.grid(row=8, column=0, sticky='E')
    unit.set("units..")

    weight_get = weight.get()
    height_get = height.get()

    Label(inform, text='\n',font="Mali 12",bg="#660000",fg="#FFFFFF").grid(row=11,column=0)

    def main():
        noti = messagebox.askyesno("Check!",'Save this information?')
    if True:
        pass
         ###ใส่พวก check
    else:
        noti.destroyed()

    submit = Button(inform, text="Submit",bg="#FFFFFF",fg="#660000",font ="consolas 10",command=main).grid(row=11,column=0)
    down = PhotoImage(file="ploo.png")

    Label(inform, image=down,borderwidth=0).grid(row=12,column=0)
    inform.mainloop()

inform()
