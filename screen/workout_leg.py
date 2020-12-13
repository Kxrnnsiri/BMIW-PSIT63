# ออกกำลังกายขา

from tkinter import *
import theme

def workoutLeg(main_window):
    def openlink_3():
        window.destroy()
        detailLeg()

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย เฉพาะส่วนขา')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_3 = Button(
        window,
        text = 'Lateral Lunges',
        font = 'Kanit',
        bg = '#FFF5F1',
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    poselink_3 = Button(
        window,
        text = 'Plie Squats',
        font = 'Prompt',
        fg = '#894C41',
        bg = '#FFE5DB',
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    poselink_3 = Button(
        window,
        text = 'Leg Swings',
        font = 'Prompt',
        fg = '#ffffff',
        bg = '#FFA691',
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    poselink_3 = Button(
        window,
        text = 'Side Leg Lifts',
        font = 'Kanit',
        fg = '#590000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    poselink_3 = Button(
        window,
        text = 'Leg raises',
        font = 'Kanit',
        fg = '#660000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_3
    )
    poselink_3.pack(pady = 10)

    mainloop()
    
