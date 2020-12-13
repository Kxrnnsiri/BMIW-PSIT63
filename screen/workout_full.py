# ออกกำลังกายทั้งตัว

from tkinter import *

def workoutFull(main_window):
    window = Toplevel(main_window)
# ออกกำลังกายทั้งตัว

from tkinter import *
import theme

def workoutFull(main_window):
    def openlink_5():
        window.destroy()
        detailFull()

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย ทุกส่วน')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_5 = Button(
        window,
        text = 'Jump up Burpee',
        font = 'Kanit',
        bg = '#FFF5F1',
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    poselink_5 = Button(
        window,
        text = 'Mountain Climber',
        font = 'Prompt',
        fg = '#894C41',
        bg = '#FFE5DB',
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    poselink_5 = Button(
        window,
        text = 'Bend Side',
        font = 'Prompt',
        fg = '#ffffff',
        bg = '#FFA691',
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    poselink_5 = Button(
        window,
        text = 'Single-leg Squats',
        font = 'Kanit',
        fg = '#590000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    poselink_5 = Button(
        window,
        text = 'Curtsy Squat/Lateral Lift',
        font = 'Kanit',
        fg = '#660000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_5
    )
    poselink_5.pack(pady = 10)

    mainloop()
    
