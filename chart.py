from tkinter import*
from tkinter import messagebox
import tkinter as tk
import os

def chart():

    chart = Tk()
    chart.geometry('590x400')
    chart.title("BMIW")
    chart.configure(background='#660000')
    chart.resizable(width=False,height=False)

    chartpic1 = PhotoImage(file = "image/bodymass_red.png")
    Label(chart, image=chartpic1, borderwidth=0).grid(row=3, column=0)

    def pagecal():
        workout = 'workout.py'
        os.system(workout)

    Label(chart, text='\n',font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=4,column=0)
    Label(chart, text="Click Next to see suitable workout plan",font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=4)

    Label(chart, text='\n',font="Mali 11",bg="#660000",fg="#FFFFFF").grid(row=6,column=0)
    nextpage = Button(chart, text="Next",bg="#FFFFFF",fg="#660000",font ="consolas 10", command=pagecal).grid(row=6,column=0)

    chart.mainloop()
chart()
