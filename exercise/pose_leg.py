# ท่าออกกำลังกาย ขา


from tkinter import *
import theme
def detailLeg(check):
    def create_pose_1(img):
        explanation = """Lateral Lunges
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนแยกขาให้กว้างมากกว่าไหล่ พร้อมประสานมือไว้ข้างหน้า
            2. เคลื่อนไหวโดยการค่อย ๆ แทงเข่าไปด้านข้าง โดยที่เท้ายังตรึงอยู่กับที่
            3. เคลื่อนไหวไปอีกข้างหนึ่งที่เหลือ เท้าต้องตรึงอยู่กับที่เช่นกัน
        จำนวนเซ็ต : เซ็ตละ 10 - 15 ครั้ง ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseLeg_1,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseLeg_1,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_next = Button(poseLeg_1,
            text = 'Next',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_2(img):
        explanation = """Plie Squats
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ท่านี้ให้เราเริ่มจากกางขาทั้งสองข้างออกจากกันระยะห่างเท่ากับมือที่กางออกสองข้าง
            ปลายเท้าชี้ออกไปด้านข้าง
            2. นำมือทั้งสองข้างมาประสานกันข้างหน้า
            3. จากนั้นย่อตัวลงให้เข่าชี้ออก ขาตั้งฉากกัน 90 องศา แล้วยืดตัวขึ้น
        จำนวนเซ็ต : เซ็ตละ 10 - 15 ครั้ง ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseLeg_2,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseLeg_2,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseLeg_2,
            text = 'Previous',
            command = call_page_1,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseLeg_2,
        text = 'Next',
        command = call_page_3,
        fg = theme.fg_pose,
        bg = theme.bg_next,
        font = theme.fontThai_2,
        padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_3(img):
        explanation = """Leg Swings
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรง แขนทั้งสองข้างเท้าเอว ทิ้งน้ำหนักตัวลงที่ขาข้างเดียว
            ขาอีกข้างหนึ่งยกขึ้นเหนือพื้นแล้วไขว้มาด้านหน้า
            2. จากนั้นเตะขาขึ้นมาด้านข้างให้สูงมากที่สุด โดยที่ขายังเหยียดตรงแล้วทรงตัวไว้อยู่
            3. สวิงขาลงมาไขว้ด้านหน้าเหมือนเดิมในท่าแรกเริ่ม
        จำนวนเซ็ต : เซ็ตละ 10 - 15 ครั้ง ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseLeg_3,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseLeg_3,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseLeg_3,
            text = 'Previous',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseLeg_3,
            text = 'Next',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_4(img):
        explanation = """Side Leg Lifts
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. เตรียมตัวอยู่ในท่านอนตะแคงข้าง เหยียดตัวตรง ยกแขนยันศีรษะไว้หนึ่งข้างให้ข้อศอกตรงกับไหล่
            2. จากนั้นยกขาฝั่งด้านบนขึ้นและลง ให้เกร็งขาและจิกปลายเท้าให้เหยียดตรงตลอดเวลา
        จำนวนเซ็ต : เซ็ตละ 10 - 15 ครั้ง ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseLeg_4,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseLeg_4,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseLeg_4,
            text = 'Previous',
            command = call_page_3,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseLeg_4,
            text = 'Next',
            command = call_page_5,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_5(img):
        explanation = """Leg raises
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนราบ แขนทั้งสองข้างแนบลำตัว แบมือออกเล็กน้อย นำมือที่คว่ำลงสอดไปไว้ใต้ก้น
            2. ยกขาทั้งสองข้างขึ้นในลักษณะเหยียดตรง เท้าชี้ขึ้นบนเพดาน เกร็งขาค้างไว้สักครู่หนึ่ง
            แล้วค่อย ๆ ลดขาลงช้า ๆ ให้กลับเข้าสู่ท่าปกติ
        จำนวนเซ็ต : เซ็ตละ 20 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseLeg_5,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseLeg_5,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)

        btn_back = Button(poseLeg_5,
            text = 'Previous',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)


    def call_page_1():
        poseLeg_2.grid_forget()
        poseLeg_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseLeg_1.grid_forget()
        poseLeg_3.grid_forget()
        poseLeg_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseLeg_2.grid_forget()
        poseLeg_4.grid_forget()
        poseLeg_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_4():
        poseLeg_3.grid_forget()
        poseLeg_5.grid_forget()
        poseLeg_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_5():
        poseLeg_4.grid_forget()
        poseLeg_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# หน้าต่าง window หลัก
    window = Tk()
    window.title('ท่าออกกำลังกาย เฉพาะส่วน ขา')
    window.configure(background = theme.background_color)

    img_1 = PhotoImage(master = window, file = "assets/leg1.png") ## ใส่รูปภาพ
    poseLeg_1 = Frame(window, bg = theme.bgcolor_detail)
    poseLeg_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_2 = PhotoImage(master = window, file = "assets/leg2.png") ## ใส่รูปภาพ
    poseLeg_2 = Frame(window, bg = theme.bgcolor_detail)
    poseLeg_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_3 = PhotoImage(master = window, file = "assets/leg3.png") ## ใส่รูปภาพ
    poseLeg_3 = Frame(window, bg = theme.bgcolor_detail)
    poseLeg_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_4 = PhotoImage(master = window, file = "assets/leg4.png") ## ใส่รูปภาพ
    poseLeg_4 = Frame(window, bg = theme.bgcolor_detail)
    poseLeg_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_5 = PhotoImage(master = window, file = "assets/leg5.png") ## ใส่รูปภาพ
    poseLeg_5 = Frame(window, bg = theme.bgcolor_detail)
    poseLeg_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_1(img_1)
    create_pose_2(img_2)
    create_pose_3(img_3)
    create_pose_4(img_4)
    create_pose_5(img_5)

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นตามค่าของ check
    if check == 1:
        poseLeg_2.grid_forget()
        poseLeg_3.grid_forget()
        poseLeg_4.grid_forget()
        poseLeg_5.grid_forget()
    elif check == 2:
        poseLeg_1.grid_forget()
        poseLeg_3.grid_forget()
        poseLeg_4.grid_forget()
        poseLeg_5.grid_forget()
    elif check == 3:
        poseLeg_1.grid_forget()
        poseLeg_2.grid_forget()
        poseLeg_4.grid_forget()
        poseLeg_5.grid_forget()
    elif check == 4:
        poseLeg_1.grid_forget()
        poseLeg_2.grid_forget()
        poseLeg_3.grid_forget()
        poseLeg_5.grid_forget()
    else:
        poseLeg_1.grid_forget()
        poseLeg_2.grid_forget()
        poseLeg_3.grid_forget()
        poseLeg_4.grid_forget()


    mainloop()




##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####
