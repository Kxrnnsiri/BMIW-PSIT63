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
    # window.geometry("800x500")
    window.configure(background = theme.background_color)

    img_body_1 = PhotoImage(master = window, file = "assets/arm.png") # ภาพแขน
    # img_body_2 = PhotoImage(master = window, file = "assets/___#ใส่ชื่อรูป___.png") # ภาพท้อง
    # img_body_3 = PhotoImage(master = window, file = "assets/___#ใส่ชื่อรูป___.png") # ภาพก้น/สะโพก
    # img_body_4 = PhotoImage(master = window, file = "assets/___#ใส่ชื่อรูป___.png") # ภาพขา
    # img_body_5 = PhotoImage(master = window, file = "assets/___#ใส่ชื่อรูป___.png") # ภาพร่างกายคน

    btn_arm = Button(
        window,
        image = img_body_1,
        height = 100,
        width = 100,
        command = openArm) #ปุ่มภาพแขน
    btn_arm.pack(padx = 10, pady = 10)
##
### ##   ยังรันข้างล่างไม่ได้ จนกว่าภาพจะเสร็จ

    # btn_ab = Button(
    #     window,
    #     image = img_body_2,
    #     height = 100,
    #     width = 100,
    #     command = openAb) #ปุ่มภาพท้อง
    # btn_ab.pack(padx = 10, pady = 10)

    # btn_leg = Button(
    #     window,
    #     image = img_body_3,
    #     height = 100,
    #     width = 100,
    #     command = openLeg) #ปุ่มภาพขา
    # btn_leg.pack(padx = 10, pady = 10)

    # btn_bottom = Button(
    #     window,
    #     image = img_body_4,
    #     height = 100,
    #     width = 100,
    #     command = openBottom) #ปุ่มภาพก้น
    # btn_bottom.pack(padx = 10, pady = 10)

    # btn_full = Button(
    #     window,
    #     image = img_body_5,
    #     height = 100,
    #     width = 100,
    #     command = openFull) #ปุ่มภาพ ทุกส่วนของร่างกาย
    # btn_full.pack(padx = 10, pady = 10)

    mainloop()
