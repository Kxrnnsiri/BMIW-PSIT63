# เมนูออกกำลังกายแขน

from exercise_arm.pose_arm1 import detailArm
from tkinter import *
import theme

def workoutArm(main_window):
    def openlink_1():
        window.destroy()
        detailArm()

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย เฉพาะส่วนแขน')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        font = 'Kanit',
        bg = '#FFF5F1',
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        font = 'Prompt',
        fg = '#894C41',
        bg = '#FFE5DB',
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        font = 'Prompt',
        fg = '#ffffff',
        bg = '#FFA691',
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        font = 'Kanit',
        fg = '#590000',
        bg = '#00E8F7',
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        font = 'Kanit',
        fg = '#660000',
        bg = '#00E8F7',
        command = openlink_1
    )
    poselink_1.pack(pady = 10)

    mainloop()