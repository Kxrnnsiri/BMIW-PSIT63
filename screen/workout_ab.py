# ออกกำลังกายท้อง

from tkinter import *
import theme

def workoutAb(main_window):
    def openlink_2():
        window.destroy()
        detailAb()

    window = Toplevel(main_window)
    window.title('เมนูออกกำลังกาย เฉพาะส่วนหน้าท้อง')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    poselink_2 = Button(
        window,
        text = 'reverse crunches',
        font = 'Kanit',
        bg = '#FFF5F1',
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    poselink_2 = Button(
        window,
        text = 'Raised Leg Crunch',
        font = 'Prompt',
        fg = '#894C41',
        bg = '#FFE5DB',
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    poselink_2 = Button(
        window,
        text = 'Bicycle Crunch',
        font = 'Prompt',
        fg = '#ffffff',
        bg = '#FFA691',
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    poselink_2 = Button(
        window,
        text = 'Standard Crunch',
        font = 'Kanit',
        fg = '#590000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    poselink_2 = Button(
        window,
        text = 'Elbow Plank',
        font = 'Kanit',
        fg = '#660000',
        bg = '#00E8F7',
        height = 1,
        width = 30,
        command = openlink_2
    )
    poselink_2.pack(pady = 10)

    mainloop()
