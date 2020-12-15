# ท่าออกกำลังกาย หน้าท้อง


from tkinter import *
import theme
def detailAB(check):
    def create_pose_1(img):
        explanation = """reverse crunches
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนหงาย ยกขางอเข่าตั้งฉากกับพื้น มือวางข้างลำตัว ฝ่ามือคว่ำลง
            2. หายใจออก พร้อมกับเกร็งหน้าท้องส่วนล่าง ยกให้สะโพกและขาขึ้นมาเข้าหาอก
            3. หายใจเข้า แล้วกลับสู่ท่าเริ่มต้น
            4. อย่าลืมว่าต้องโฟกัสที่หน้าท้องส่วนล่าง และอย่าใช้ฝ่ามือกดออกแรงดันตัวขึ้น
        จำนวนเซ็ต : เซ็ตละ 10 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseAB_1,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseAB_1,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Dream Inspired, https://sistacafe.com/summaries/3025]
        ###Pic.[http://img.aws.livestrongcdn.com/ls-slideshow-main-image/cme/photography.prod.demandstudios.com/b6e78136-8792-4288-b0a9-350f94adfe12.gif]

        btn_next = Button(poseAB_1,
            text = 'Next',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_2(img):
        explanation = """Raised Leg Crunch
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1.  นอนหงาย ยกขางอเข่าตั้งฉากกับพื้น มือวางไว้หลังศีรษะ หายใจเข้าและเตรียมตัวให้พร้อม
            2. หายใจออก ยกลำตัวด้านบนขึ้น โดยสะโพกและขาตึงอยู่กับที่ อย่าให้คางแตะอก
            3. ลดตัวลงกลับที่เดิม แล้วหายใจเข้า ทำซ้ำ
        จำนวนเซ็ต : เซ็ตละ 10 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseAB_2,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseAB_2,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Dream Inspired, https://sistacafe.com/summaries/3025]
        ###Pic.[http://img.aws.livestrongcdn.com/ls-slideshow-main-image/cme/photography.prod.demandstudios.com/a39d823e-f0e5-405c-99ac-07f9c7db0f0a.gif]

        btn_back = Button(poseAB_2,
            text = 'Previous',
            command = call_page_1,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseAB_2,
        text = 'Next',
        command = call_page_3,
        fg = theme.fg_pose,
        bg = theme.bg_next,
        font = theme.fontThai_2,
        padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_3(img):
        explanation = """Bicycle Crunch
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนหงายลงบนพื้น มืออยู่หลังศีรษะ
            2. เกร็งหน้าท้องส่วนล่างเพื่อยกขาขึ้นจากพื้นเล็กน้อย
            3. บิดลำตัว และงอเข่าซ้ายขึ้น พร้อม ๆ กับหันศอกขวาเข้าหาเข่าซ้าย แล้วสลับข้าง
        จำนวนเซ็ต : เซ็ตละ 10 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseAB_3,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseAB_3,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Dream Inspired, https://sistacafe.com/summaries/3025]
        ###Pic.[http://img.aws.livestrongcdn.com/ls-slideshow-main-image/cme/photography.prod.demandstudios.com/4892ee9f-412e-470f-beaa-ed92e5b7a62d.gif]

        btn_back = Button(poseAB_3,
            text = 'Previous',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseAB_3,
            text = 'Next',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_4(img):
        explanation = """Standard Crunch
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนหงาย งอเข่าชี้ไปที่เพดาน
            2. มือวางไว้หลังศีรษะ ศอกหันออกด้านข้าง มือแตะศีรษะได้ แต่อย่าช่วยออกแรงดันขึ้นขณะซิทอัพ
            3. หายใจออก เกร็งหน้าท้อง แล้วยกส่วนไหล่และศีรษะขึ้น คองอได้เล็กน้อย แต่อย่าใกล้อกเกินไป
            4. หายใจเข้า พร้อม ๆ กับลดศีรษะลงไปที่พื้น แล้วทำซ้ำทันที
        จำนวนเซ็ต : เซ็ตละ 10 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseAB_4,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseAB_4,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Dream Inspired, https://sistacafe.com/summaries/3025]
        ###Pic.[http://img.aws.livestrongcdn.com/ls-slideshow-main-image/cme/photography.prod.demandstudios.com/929cc1dd-f0fe-49d5-b2b7-18101d48074a.gif]

        btn_back = Button(poseAB_4,
            text = 'Previous',
            command = call_page_3,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseAB_4,
            text = 'Next',
            command = call_page_5,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_5(img):
        explanation = """Elbow Plank
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. นอนคว่ำ วางแขนลงชันไว้กับพื้น
            2. ยกลำตัวเป็นเส้นตรงขนานกับพื้น ห้ามกั้นหายใจ
        จำนวนเซ็ต : 30 วินาที ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseAB_5,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseAB_5,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[https://www.siphhospital.com/th/news/article/share/861]
        ###Pic.[https://i.pinimg.com/originals/02/67/a1/0267a1d9d3eda030b4a5b578a6985cc8.jpg]

        btn_back = Button(poseAB_5,
            text = 'Previous',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)


    def call_page_1():
        poseAB_2.grid_forget()
        poseAB_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseAB_1.grid_forget()
        poseAB_3.grid_forget()
        poseAB_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseAB_2.grid_forget()
        poseAB_4.grid_forget()
        poseAB_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_4():
        poseAB_3.grid_forget()
        poseAB_5.grid_forget()
        poseAB_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_5():
        poseAB_4.grid_forget()
        poseAB_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# หน้าต่าง window หลัก
    window = Tk()
    window.title('ท่าออกกำลังกาย เฉพาะส่วน หน้าท้อง')
    window.configure(background = theme.background_color)

    img_1 = PhotoImage(master = window, file = "assets/ab1.png") ## ใส่รูปภาพ
    poseAB_1 = Frame(window, bg = theme.bgcolor_detail)
    poseAB_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_2 = PhotoImage(master = window, file = "assets/ab2.png") ## ใส่รูปภาพ
    poseAB_2 = Frame(window, bg = theme.bgcolor_detail)
    poseAB_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_3 = PhotoImage(master = window, file = "assets/ab3.png") ## ใส่รูปภาพ
    poseAB_3 = Frame(window, bg = theme.bgcolor_detail)
    poseAB_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_4 = PhotoImage(master = window, file = "assets/ab4.png") ## ใส่รูปภาพ
    poseAB_4 = Frame(window, bg = theme.bgcolor_detail)
    poseAB_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_5 = PhotoImage(master = window, file = "assets/ab5.png") ## ใส่รูปภาพ
    poseAB_5 = Frame(window, bg = theme.bgcolor_detail)
    poseAB_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_1(img_1)
    create_pose_2(img_2)
    create_pose_3(img_3)
    create_pose_4(img_4)
    create_pose_5(img_5)

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นตามค่าของ check
    if check == 1:
        poseAB_2.grid_forget()
        poseAB_3.grid_forget()
        poseAB_4.grid_forget()
        poseAB_5.grid_forget()
    elif check == 2:
        poseAB_1.grid_forget()
        poseAB_3.grid_forget()
        poseAB_4.grid_forget()
        poseAB_5.grid_forget()
    elif check == 3:
        poseAB_1.grid_forget()
        poseAB_2.grid_forget()
        poseAB_4.grid_forget()
        poseAB_5.grid_forget()
    elif check == 4:
        poseAB_1.grid_forget()
        poseAB_2.grid_forget()
        poseAB_3.grid_forget()
        poseAB_5.grid_forget()
    else:
        poseAB_1.grid_forget()
        poseAB_2.grid_forget()
        poseAB_3.grid_forget()
        poseAB_4.grid_forget()


    mainloop()




##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####
