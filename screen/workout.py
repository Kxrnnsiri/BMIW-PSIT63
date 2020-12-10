# หน้าขึ้น 5 รูป

from tkinter import *
from screen.workout_arm import workoutArm
import theme

def workoutSelector():
    # ฟังก์ชันเปิดหน้าต่าง workoutArm
    def openArm():
        workoutArm(window)

    window = Tk()
    window.title('เมนูออกกำลังกาย')
    # window.geometry("800x500")
    window.configure(background = theme.background_color)

    img_body = PhotoImage(master = window, file = "assets/arm.png") # ภาพแขน

    btn_arm = Button(
        window,
        image = img_body,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพแขน
    btn_arm.pack(padx = 10, pady = 10)

    btn_ab = Button(
        window,
        image = img_body,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพท้อง
    btn_ab.pack(padx = 10, pady = 10)

    btn_leg = Button(
        window,
        image = img_body,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพขา
    btn_leg.pack(padx = 10, pady = 10)

    btn_bottom = Button(
        window,
        image = img_body,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพก้น
    btn_bottom.pack(padx = 10, pady = 10)

    btn_full = Button(
        window,
        image = img_body,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพ ทุกส่วนของร่างกาย
    btn_full.pack(padx = 10, pady = 10)
    # btn_arm.place(height=100, width=100)

    # btn_leg = Button(window, image = img_body, command = openLeg) #ปุ่มภาพแขน
    # btn_leg.pack()

    mainloop()
