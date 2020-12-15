from tkinter import*
from tkinter import messagebox
import tkinter as tk
import os

def inform():

    inform = Tk()
    inform.geometry('590x700')
    inform.title("BMIW")
    inform.configure(background='#660000')
    inform.resizable(width=False,height=False)

    header = PhotoImage(file = "You Inform1.png")
    Label(inform, image=header, borderwidth=0).grid(row=1, column=0)


    Label(inform, text='\n',font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=2,column=0)
    Label(inform, text="Enter Your Weight (kg.) :"+"       "*6,font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=3)
    Label(inform, text='\n',font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=3,column=0)
    Label(inform, text="Enter Your Height (cm.) :"+"       "*6,font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=6)
    Label(inform, text='\n',font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=6,column=0)

    weight = tk.DoubleVar()
    weight.set("")
    height = tk.DoubleVar()
    height.set("")
    bmires = tk.DoubleVar()

    weight_ent = tk.Entry(inform, textvariable=weight, font="consolas 12", bg="#FFFFFF",fg="#660000").grid(row=4)
    height_ent = tk.Entry(inform, textvariable=height, font="consolas 12", bg="#FFFFFF",fg="#660000").grid(row=8)

        ## ref for input entry : https://stackoverflow.com/questions/47378715/tkinter-how-to-get-the-value-of-an-entry-widget

    def pagecal():
        chart = 'chart.py'
        os.system(chart)

    # def endpage():
    #         pagecal()
    #         inform.destroy()

    def bmi_calculator():

        bmi = weight.get()/((height.get()/100)**2)

        resulthead = tk.Label(inform, text= 'Your bmi is',font="Mali 11",bg="Blue",fg="#FFFFFF").grid(row=13,column=0,ipadx=245)
        bmires = tk.Label(inform, text= bmi, font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=14,column=0)

        chart = Button(inform, text="Next",bg="#FFFFFF",fg="#660000",font ="consolas 10", command=pagecal).grid(row=15,column=0)

        return resulthead and bmires and chart

    Label(inform, text='\n',font="Mali 8",bg="#660000",fg="#FFFFFF").grid(row=10,column=0)

    submit = Button(inform, text="Submit",bg="#FFFFFF",fg="#660000",font ="consolas 10", command=bmi_calculator).grid(row=11,column=0)

    Label(inform, text='\n',font="Mali 8",bg="#660000",fg="#FFFFFF").grid(row=12,column=0)
    inform.mainloop()

inform()
