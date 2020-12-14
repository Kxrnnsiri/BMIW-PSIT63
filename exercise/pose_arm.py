# ท่าออกกำลัง แขน

from tkinter import *
import theme
def detailArm(check):
    def create_pose_arm_1(img):
        explanation = """นั่งกลางอากาศ
        อุปกรณ์ : เก้าอี้ หรือ ม้านั่ง
        วิธีทำ : 
            1. วางเก้าอี้ไว้ด้านหลัง ยืดแขนทั้งสองข้างบนเก้าอี้ ส้นเท้าสองข้างยันพื้นไว้ ช่วงต้นขา และน่องตั้งฉากกัน
            2. เกร็งแขน และลำตัวไว้ ค่อย ๆ ย่อตัวลงด้านหน้าเก้าอี้ เหมือนกำลังนั่งลงบนอากาศ
            3. เสร็จแล้วค่อย ๆ ยกตัวขึ้นในท่าเดิม
        จำนวนเซ็ต : เซ็ตละ 10 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseArm_1,
            image = img,
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

        btn_next = Button(poseArm_1,
            text = 'Next',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_2(img):
        explanation = """กระชับต้นแขน
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรง แยกขาให้กว้างเท่าไหล่ กางแขนทั้งสองข้าง
            2. เหยียดแขนทั้งสองข้างไปด้านหลังให้ตึง
            3. เหวี่ยงแขนทั้งสองข้างพร้อม ๆ กัน เป็นวงกลม
        จำนวนเซ็ต : เซ็ตละ 20 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseArm_2,
            image = img,
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

        btn_back = Button(poseArm_2,
            text = 'Previous',
            command = call_page_1,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseArm_2,
        text = 'Next',
        command = call_page_3,
        fg = theme.fg_pose,
        bg = theme.bg_next,
        font = theme.fontThai_2,
        padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_3(img):
        explanation = """ลดแขนย้อย
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรง ขาชิดกัน กางแขนทั้งสองข้างไปด้านข้าง
            2. หุบแขน สลับขึ้นลงไปเรื่อย ๆ
        จำนวนเซ็ต : เซ็ตละ 20 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseArm_3,
            image = img,
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

        btn_back = Button(poseArm_3,
            text = 'Previous',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseArm_3,
            text = 'Next',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_4(img):
        explanation = """กระชับแขน ลดปีกหลัง
        อุปกรณ์ : ไม่มี
        วิธีทำ : 
            1. ยืนตรง กางแขนไปด้านหน้า
            2. หุบแขนลงวางข้างลำตัว จากนั้นยกแขนเหยียดไปด้านหลัง แล้วดึงแขนกลับข้างลำตัว
        จำนวนเซ็ต : เซ็ตละ 20 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseArm_4,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseArm_4,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseArm_4,
            text = 'Previous',
            command = call_page_3,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseArm_4,
            text = 'Next',
            command = call_page_5,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_arm_5(img):
        explanation = """ว่ายน้ำ
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนคว่ำ ยืดแขนทั้งสองข้างไปด้านหน้า เกร็งหน้าท้อง
            2. ยกลำตัวด้านบนและด้านล่างขึ้นจากพื้นเล็กน้อย
            3. ขยับแขนทั้งสองข้างและขาทั้งสองข้างขึ้นลง
        จำนวนเซ็ต : ทำติดต่อกัน 1 นาที ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseArm_5,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseArm_5,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseArm_5,
            text = 'Previous',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)


    def call_page_1():
        poseArm_2.grid_forget()
        poseArm_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseArm_1.grid_forget()
        poseArm_3.grid_forget()
        poseArm_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseArm_2.grid_forget()
        poseArm_4.grid_forget()
        poseArm_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_4():
        poseArm_3.grid_forget()
        poseArm_5.grid_forget()
        poseArm_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_5():
        poseArm_4.grid_forget()
        poseArm_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# หน้าต่าง window หลัก
    window = Tk()
    window.title('ท่าออกกำลังกาย เฉพาะส่วน แขน')
    window.configure(background = theme.background_color)

    img_1 = PhotoImage(master = window, file = "assets/arm1.png") ## ใส่รูปภาพ
    poseArm_1 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_2 = PhotoImage(master = window, file = "assets/arm2.png") ## ใส่รูปภาพ
    poseArm_2 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_3 = PhotoImage(master = window, file = "assets/arm3.png") ## ใส่รูปภาพ
    poseArm_3 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_4 = PhotoImage(master = window, file = "assets/arm4.png") ## ใส่รูปภาพ
    poseArm_4 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_5 = PhotoImage(master = window, file = "assets/arm5.png") ## ใส่รูปภาพ
    poseArm_5 = Frame(window, bg = theme.bgcolor_detail)
    poseArm_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_arm_1(img_1)
    create_pose_arm_2(img_2)
    create_pose_arm_3(img_3)
    create_pose_arm_4(img_4)
    create_pose_arm_5(img_5)

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นตามค่าของ check
    if check == 1:
        poseArm_2.grid_forget()
        poseArm_3.grid_forget()
        poseArm_4.grid_forget()
        poseArm_5.grid_forget()
    elif check == 2:
        poseArm_1.grid_forget()
        poseArm_3.grid_forget()
        poseArm_4.grid_forget()
        poseArm_5.grid_forget()
    elif check == 3:
        poseArm_1.grid_forget()
        poseArm_2.grid_forget()
        poseArm_4.grid_forget()
        poseArm_5.grid_forget()
    elif check == 4:
        poseArm_1.grid_forget()
        poseArm_2.grid_forget()
        poseArm_3.grid_forget()
        poseArm_5.grid_forget()
    else:
        poseArm_1.grid_forget()
        poseArm_2.grid_forget()
        poseArm_3.grid_forget()
        poseArm_4.grid_forget()


    mainloop()




##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####
