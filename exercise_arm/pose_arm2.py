# ท่าออกกำลัง แขน ท่าที่ 2
### หน้านี้ไม่เกี่ยววววววว

from tkinter import *
from exercise_arm.pose_arm3 import detailArm_3
import theme

def detailArm_2(prev_function):
    def backpose():
        window.destroy()
        prev_function()
    def nextpose():
        window.destroy()
        detailArm_3(detailArm_2)

    window = Tk()
    window.title('ชื่อท่า .......2') ## ใส่ชื่อท่า
    window.configure(background = theme.background_color)
    imgitem = PhotoImage(master = window, file = "assets/arm.png") ## ใส่ชื่อรูป
    explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด

    Label(
        window,
        image = imgitem,
        width = 100,
        height = 100,
        padx = 10
    ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)

    Label(
        window,
        justify = 'left',
        text = explanation,
        font = theme.fontThai_2,
        bg = theme.bgcolor_detail,
        padx = 20,
        pady = 20
    ).grid(row = 0, column = 1, padx = 10, pady = 10)

    btn_back = Button(
        window,
        text = 'Previous',
        command = backpose,
        padx = 10
    )
    btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

    btn_next = Button(
        window,
        text = 'Next',
        command = nextpose,
        fg = 'blue',
        padx = 10
    )
    btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    mainloop()
