# หน้าขึ้น 5 รูป

from tkinter import *
from screen.workout_arm import workoutArm
import theme

def workoutSelector():
    # ฟังก์ชันเปิดหน้าต่าง workoutArm
    def openArm():
        workoutArm(window)

    window = Tk()
    window.configure(background = theme.background_color)

    img_body = PhotoImage(master = window, file = "assets/arm.png") # ภาพแขน

    btn_arm = Button(window, image = img_body, command = openArm) #ปุ่มภาพแขน
    btn_arm.pack()

    # btn_leg = Button(window, image = img_body, command = openLeg) #ปุ่มภาพแขน
    # btn_leg.pack()

    mainloop()
