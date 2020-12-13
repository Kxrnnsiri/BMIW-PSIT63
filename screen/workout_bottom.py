# ออกกำลังกายก้น

from tkinter import *
import theme

def workoutBottom(main_window):
    def openlink_4():
        window.destroy()
        detailbottom()

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย เฉพาะส่วนสะโพก')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_4 = Button(
        window,
        text = 'Squats',
        font = 'Kanit',
        bg = '#FFF5F1',
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    poselink_4 = Button(
        window,
        text = 'Curtsy Squats',
        font = 'Prompt',
        fg = '#894C41',
        bg = '#FFE5DB',
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    poselink_4 = Button(
        window,
        text = 'Sumo walk',
        font = 'Prompt',
        fg = '#ffffff',
        bg = '#FFA691',
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    poselink_4 = Button(
        window,
        text = 'Glute Bridge',
        font = 'Kanit',
        fg = '#590000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    poselink_4 = Button(
        window,
        text = 'Ski Squats',
        font = 'Kanit',
        fg = '#660000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_4
    )
    poselink_4.pack(pady = 10)

    mainloop()
    
