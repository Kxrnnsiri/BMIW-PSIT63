# ท่าออกกำลังกาย สะโพก


from tkinter import *
import theme
def detailBottom(check):
    def create_pose_1(img):
        explanation = """##____ชื่อท่า___##
        Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseBottom_1,
            image = img,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseBottom_1,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_next = Button(poseBottom_1,
            text = 'Next',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_2(img):
        explanation = """##____ชื่อท่า___##
        Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseBottom_2,
            image = img,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseBottom_2,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseBottom_2,
            text = 'Previous',
            command = call_page_1,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseBottom_2,
        text = 'Next',
        command = call_page_3,
        fg = theme.fg_pose,
        bg = theme.bg_next,
        font = theme.fontThai_2,
        padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_3(img):
        explanation = """##____ชื่อท่า___##
        Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseBottom_3,
            image = img,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseBottom_3,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseBottom_3,
            text = 'Previous',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseBottom_3,
            text = 'Next',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_4(img):
        explanation = """##____ชื่อท่า___##
        Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseBottom_4,
            image = img,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseBottom_4,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseBottom_4,
            text = 'Previous',
            command = call_page_3,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseBottom_4,
            text = 'Next',
            command = call_page_5,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_5(img):
        explanation = """##____ชื่อท่า___##
        Label ฉันจะเป็นนกจะได้บินได้ เมื่อไรจะเสร็จสักที อาฮ๊าาาา ~~~""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseBottom_5,
            image = img,
            width = 100,
            height = 100,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseBottom_5,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseBottom_5,
            text = 'Previous',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)


    def call_page_1():
        poseBottom_2.grid_forget()
        poseBottom_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseBottom_1.grid_forget()
        poseBottom_3.grid_forget()
        poseBottom_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseBottom_2.grid_forget()
        poseBottom_4.grid_forget()
        poseBottom_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_4():
        poseBottom_3.grid_forget()
        poseBottom_5.grid_forget()
        poseBottom_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_5():
        poseBottom_4.grid_forget()
        poseBottom_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# หน้าต่าง window หลัก
    window = Tk()
    window.title('ท่าออกกำลังกาย เฉพาะส่วน สะโพก')
    window.configure(background = theme.background_color)

    img_1 = PhotoImage(master = window, file = "assets/arm.png") ## ใส่รูปภาพ
    poseBottom_1 = Frame(window, bg = theme.bgcolor_detail)
    poseBottom_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_2 = PhotoImage(master = window, file = "assets/arm.png") ## ใส่รูปภาพ
    poseBottom_2 = Frame(window, bg = theme.bgcolor_detail)
    poseBottom_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_3 = PhotoImage(master = window, file = "assets/arm.png") ## ใส่รูปภาพ
    poseBottom_3 = Frame(window, bg = theme.bgcolor_detail)
    poseBottom_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_4 = PhotoImage(master = window, file = "assets/arm.png") ## ใส่รูปภาพ
    poseBottom_4 = Frame(window, bg = theme.bgcolor_detail)
    poseBottom_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_5 = PhotoImage(master = window, file = "assets/arm.png") ## ใส่รูปภาพ
    poseBottom_5 = Frame(window, bg = theme.bgcolor_detail)
    poseBottom_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_1(img_1)
    create_pose_2(img_2)
    create_pose_3(img_3)
    create_pose_4(img_4)
    create_pose_5(img_5)

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นตามค่าของ check
    if check == 1:
        poseBottom_2.grid_forget()
        poseBottom_3.grid_forget()
        poseBottom_4.grid_forget()
        poseBottom_5.grid_forget()
    elif check == 2:
        poseBottom_1.grid_forget()
        poseBottom_3.grid_forget()
        poseBottom_4.grid_forget()
        poseBottom_5.grid_forget()
    elif check == 3:
        poseBottom_1.grid_forget()
        poseBottom_2.grid_forget()
        poseBottom_4.grid_forget()
        poseBottom_5.grid_forget()
    elif check == 4:
        poseBottom_1.grid_forget()
        poseBottom_2.grid_forget()
        poseBottom_3.grid_forget()
        poseBottom_5.grid_forget()
    else:
        poseBottom_1.grid_forget()
        poseBottom_2.grid_forget()
        poseBottom_3.grid_forget()
        poseBottom_4.grid_forget()


    mainloop()




##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####