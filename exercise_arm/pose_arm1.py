# ท่าออกกำลัง แขน ท่าที่ 1

from tkinter import *
import theme
def detailArm():
    def create_pose_arm_1():
        ## ใส่ชื่อรูป
        imgitem = PhotoImage(master = window, file = "assets/arm.png")
        ## ใส่เนื้อหา/รายละเอียด
        explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~"""
        Label(
            poseArm_1,
            image = imgitem,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseArm_1,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_next = Button(poseArm_1, text = 'Next', command = call_page_2, fg = 'blue', padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_2():
        ## ใส่ชื่อรูป
        imgitem = PhotoImage(master = poseArm_2, file = "assets/arm.png")
        ## ใส่เนื้อหา/รายละเอียด
        explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~"""
        Label(
            poseArm_2,
            image = imgitem,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseArm_2,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseArm_2, text = 'Previous', command = call_page_1, padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseArm_2, text = 'Next', command = call_page_3, fg = 'blue', padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_3():
        ## ใส่ชื่อรูป
        imgitem = PhotoImage(master = poseArm_3, file = "assets/arm.png")
        ## ใส่เนื้อหา/รายละเอียด
        explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~"""
        Label(
            poseArm_3,
            image = imgitem,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseArm_3,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseArm_3, text = 'Previous', command = call_page_2, padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseArm_3, text = 'Next', command = call_page_3, fg = 'blue', padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def call_page_1():
        poseArm_2.grid_forget()
        poseArm_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseArm_1.grid_forget()
        poseArm_3.grid_forget()
        poseArm_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseArm_2.grid_forget()
        poseArm_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    window = Tk()
    window.title('ท่าออกกำลังกาย เฉพาะส่วน แขน')
    window.configure(background = theme.background_color)

    poseArm_1 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    poseArm_2 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    poseArm_3 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_arm_1()
    create_pose_arm_2()
    create_pose_arm_3()

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นอันแรก
    poseArm_2.grid_forget()
    poseArm_3.grid_forget()

    mainloop()


    # imgitem = PhotoImage(master = window, file = "assets/arm.png") ## ใส่ชื่อรูป
    # explanation = """Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด

##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####