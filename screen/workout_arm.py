# เมนูออกกำลังกายแขน

from exercise.pose_arm import detailArm
from tkinter import *
import theme

def workoutArm(main_window):
    def openlink_1():
        link = 1
        window.destroy()
        detailArm(link)
    def openlink_2():
        link = 2
        window.destroy()
        detailArm(link)
    def openlink_3():
        link = 3
        window.destroy()
        detailArm(link)
    def openlink_4():
        link = 4
        window.destroy()
        detailArm(link)
    def openlink_5():
        link = 5
        window.destroy()
        detailArm(link)

    window = Toplevel(main_window)
    window.title('BMIW: Arms Workout')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_1 = Button(
        window,
        text = 'นั่งกลางอากาศ',  ## ใส่ ชื่อ ท่า
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
        text = 'กระชับต้นแขน',  ## ใส่ ชื่อ ท่า
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
        text = 'ลดแขนย้อย',  ## ใส่ ชื่อ ท่า
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
        text = 'กระชับแขน ลดปีกหลัง',  ## ใส่ ชื่อ ท่า
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
        text = 'ว่ายน้ำ',  ## ใส่ ชื่อ ท่า
        font = theme.fontThai_2,
        fg = theme.fg_menu,
        bg = theme.bg_menu,
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    mainloop()
