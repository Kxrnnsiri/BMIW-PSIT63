# หน้าขึ้น 5 รูป

from tkinter import *
from screen.workout_arm import workoutArm
from screen.workout_ab import workoutAb
from screen.workout_leg import workoutLeg
from screen.workout_bottom import workoutBottom
from screen.workout_full import workoutFull
import theme

def workoutSelector():
    # ฟังก์ชันเปิดหน้าต่าง workoutArm
    def openArm():
        workoutArm(window)
    def openAb():
        workoutAb(window)
    def openLeg():
        workoutLeg(window)
    def openBottom():
        workoutBottom(window)
    def openFull():
        workoutFull(window)

    window = Tk()
    window.title('เมนูออกกำลังกาย')
    window.configure(background = theme.background_color)

    img_body_1 = PhotoImage(master = window, file = "assets/arm_2.png") # ภาพแขน
    img_body_2 = PhotoImage(master = window, file = "assets/abs.png") # ภาพท้อง
    img_body_3 = PhotoImage(master = window, file = "assets/leg_1.png") # ภาพขา
    img_body_4 = PhotoImage(master = window, file = "assets/butt.png") # ภาพสะโพก
    img_body_5 = PhotoImage(master = window, file = "assets/body_3.png") # ภาพร่างกายคน

    btn_arm = Button(
        window,
        image = img_body_1,
        height = 150,
        width = 100,
        command = openArm) #ปุ่มภาพแขน
    btn_arm.grid(row = 0, column = 0, padx = 10, pady = 10)

    btn_ab = Button(
        window,
        image = img_body_2,
        height = 150,
        width = 100,
        command = openAb) #ปุ่มภาพท้อง
    btn_ab.grid(row = 0, column = 1, padx = 10, pady = 10)

    btn_leg = Button(
        window,
        image = img_body_3,
        height = 150,
        width = 100,
        command = openLeg) #ปุ่มภาพขา
    btn_leg.grid(row = 1, column = 0, padx = 10, pady = 10)

    btn_bottom = Button(
        window,
        image = img_body_4,
        height = 150,
        width = 100,
        command = openBottom) #ปุ่มภาพก้น
    btn_bottom.grid(row = 1, column = 1, padx = 10, pady = 10)

    btn_full = Button(
        window,
        image = img_body_5,
        height = 150,
        width = 100,
        command = openFull) #ปุ่มภาพ ทุกส่วนของร่างกาย
    btn_full.grid(row = 2, columnspan = 2, sticky = S, padx = 10, pady = 10)

    mainloop()
