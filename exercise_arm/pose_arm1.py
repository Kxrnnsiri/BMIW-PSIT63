# ท่าออกกำลัง แขน ท่าที่ 1

from tkinter import *
import theme

def detailArm_1():
    window = Tk()
    imageitem = PhotoImage(master = window, file = "assets/arm.png")
    explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~"""
    Label(
        window,
        image = imageitem,
        width = 100,
        height = 100
    ).pack(side = 'right')
    Label(
        window,
        justify = 'left',
        padx = 20,
        pady = 20,
        text = explanation
    ).pack(side = 'left')
