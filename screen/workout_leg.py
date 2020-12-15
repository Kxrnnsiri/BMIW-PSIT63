# ออกกำลังกายขา

from exercise.pose_leg import detailLeg
from tkinter import *
import theme

def workoutLeg(main_window):
    def openlink_1():
        link = 1
        window.destroy()
        detailLeg(link)
    def openlink_2():
        link = 2
        window.destroy()
        detailLeg(link)
    def openlink_3():
        link = 3
        window.destroy()
        detailLeg(link)
    def openlink_4():
        link = 4
        window.destroy()
        detailLeg(link)
    def openlink_5():
        link = 5
        window.destroy()
        detailLeg(link)

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย เฉพาะส่วน ขา')
    window.geometry('480x400')
    window.configure(background = theme.background_color)

    poselink_1 = Button(
        window,
        text = 'Lateral Lunges',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    poselink_2 = Button(
        window,
        text = 'Plie Squats',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    poselink_3 = Button(
        window,
        text = 'Leg Swings',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    poselink_4 = Button(
        window,
        text = 'Side Leg Lifts',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    poselink_5 = Button(
        window,
        text = 'Leg raises',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    mainloop()
