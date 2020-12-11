# ออกกำลังกายแขน

from exercise_arm.pose_arm1 import detailArm_1
from tkinter import *
import theme

def workoutArm(main_window):
    def openlink_1():
        window.destroy()
        detailArm_1()

    window = Toplevel(main_window)
    window.title('ท่าออกกำลังกาย เฉพาะส่วนแขน')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        command = openlink_1
    )
    poselink_1.pack(pady = 20)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        command = openlink_1
    )
    poselink_1.pack(pady = 20)

    poselink_1 = Button(
        window,
        text = 'ชื่อท่าออกกำลังกาย',
        command = openlink_1
    )
    poselink_1.pack(pady = 20)


    mainloop()