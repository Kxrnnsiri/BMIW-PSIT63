# ท่าออกกำลังกาย ทุกส่วน


from tkinter import *
import theme
def detailFull(check):
    def create_pose_1(img):
        explanation = """Jump up Burpee
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตัวตรง แยกขาเล็กน้อย
            2. ย่อตัวคุกเข่าลงเกือบติดพื้น โดยใช้มือทั้งสองข้างยันไว้แล้วออกแรงเลื่อนขาทั้งสองข้างไปด้านหลัง
            โดยที่มือทั้งสองข้างยังดันพื้นอยู่ ในรูปแบบของท่าวิดพื้น
            3. ออกแรงดันขากลับมาด้านหน้าแล้วลุกยืนขึ้น
            4. กระโดดชูแขน นับเป็น 1 ครั้ง
        จำนวนเซ็ต : เซ็ตละ 15 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseFull_1,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseFull_1,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Beauty Editor, https://www.wongnai.com/articles/exercise-workout-plan]
        ###Pic.[https://www.mensjournal.com/wp-content/uploads/2018/05/1380-burpee1.jpg?w=700&quality=86&strip=all&iswp=1]

        btn_next = Button(poseFull_1,
            text = 'Next',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_2(img):
        explanation = """Mountain Climber
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. เริ่มในท่าวิดพื้น ลงน้ำหนักที่มือ และนิ้วโป้งทั้งสองข้าง ยืดเข่าให้ตรง
            2. งอเข่าทำ 90 องศากับสะโพก
            3. เหยียดขาข้างที่ทึ่งออกกลับไปในท่าเตรียมวิดพื้น
            4. แล้วสลับงอเข่าอีกข้างอีกข้างทำมุม 90 องศากับสะโพก ทำขาทั้งสองข้างสลับกัน
        จำนวนเซ็ต : เซ็ตละ 15 ครั้ง ทั้งหมด 2 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseFull_2,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseFull_2,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[Beauty Editor, https://www.wongnai.com/articles/exercise-workout-plan]
        ###Pic.[https://images.everydayhealth.com/images/healthy-living/fitness/the-number-one-workout-move-you-should-be-doing-1440x810.jpg]

        btn_back = Button(poseFull_2,
            text = 'Previous',
            command = call_page_1,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseFull_2,
        text = 'Next',
        command = call_page_3,
        fg = theme.fg_pose,
        bg = theme.bg_next,
        font = theme.fontThai_2,
        padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_3(img):
        explanation = """Bend Side
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรงแยกเท้าออกกว้างกว่าไหล่เล็กน้อย จากนั้นงอเข่า ย่อตัวลง
            2. เอียงตัวไปด้านขวา ทิ้งแขนขวาลงกับพื้น ส่วนแขนซ้ายเหยียดตรงขึ้นด้านบน
            3. สลับข้าง เอียงตัวไปด้านซ้าย ทิ้งแขนซ้ายลงกับพื้น ส่วนแขนขวาเหยียดตรงขึ้นด้านบน
        จำนวนเซ็ต : เซ็ตละ 15 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseFull_3,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseFull_3,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[TrueID Women, https://women.trueid.net/detail/EP1yO79D4VR]
        ###Pic.[https://lh3.googleusercontent.com/proxy/yvPeGBU7QZZp49yPhtfEvyXGVNnPCzT1xydmCD032FaqBQkl9ImLpQAd_eYtkyJsIRso2j1ZC5wnJP18LVyI2In7amrrvNbDbEmTi7_mFEdQw_OQRgXI]

        btn_back = Button(poseFull_3,
            text = 'Previous',
            command = call_page_2,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseFull_3,
            text = 'Next',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_4(img):
        explanation = """Single-leg Squats
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรง วางข้อเท้าขวาไว้บนขาซ้าย
            2. ย่อตัวนั่งลง ทิ้งเอวและก้นไปข้างหลัง มือทั้งสองข้างเหยียดมาด้านหน้า
        จำนวนเซ็ต : เซ็ตละ 15 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseFull_4,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseFull_4,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[TrueID Women, https://women.trueid.net/detail/EP1yO79D4VR]
        ###Pic.[https://cathe.com/wp-content/uploads/2019/04/shutterstock_300575984.jpg]

        btn_back = Button(poseFull_4,
            text = 'Previous',
            command = call_page_3,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

        btn_next = Button(poseFull_4,
            text = 'Next',
            command = call_page_5,
            fg = theme.fg_pose,
            bg = theme.bg_next,
            font = theme.fontThai_2,
            padx = 10)
        btn_next.grid(row = 1, column = 1, sticky = E, padx = 10, pady = 10)

    def create_pose_5(img):
        explanation = """Curtsy Squat
        อุปกรณ์ : ไม่มี
        วิธีทำ :
            1. ยืนตรง แยกเท้าออกเล็กน้อย มือทั้งสองข้างเหยียดตรงไปด้านหน้า
            จากนั้นถอยขาขวาก้าวไปด้านหลังทางซ้าย พร้อม ๆ กับย่อเข่าลง
            2. ยืดตัว ก้าวขาขวาไปด้านหน้า เฉียงออกไปทางขวา ย่อเข่าลง เอนตัวไปด้านหน้าเล็กน้อย
            จากนั้นกลับสู่ท่ายืนตรง นับเป็น 1 ครั้ง
        จำนวนเซ็ต : เซ็ตละ 15 ครั้ง ทั้งหมด 3 เซ็ต""" ## ใส่เนื้อหา/รายละเอียด
        Label(
            poseFull_5,
            image = img,
            padx = 10
        ).grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
        Label(
            poseFull_5,
            justify = 'left',
            text = explanation,
            font = theme.fontThai_2,
            padx = 20,
            pady = 20
        ).grid(row = 0, column = 1, padx = 10, pady = 10)
        ###Cr.[TrueID Women, https://women.trueid.net/detail/EP1yO79D4VR]
        ###Pic.[https://lh3.googleusercontent.com/proxy/OHJQWWVSRCWQn5fIZfQ6Hlv1Ub19TRAwlTKUrnxRqZ_bDSx7ZiOec3KgcWoA19-adJtb9ag2zPDXLIPqJpmaoXTDmxOh3265EKllvMyQkS3UNTfzhGDr4m-X]

        btn_back = Button(poseFull_5,
            text = 'Previous',
            command = call_page_4,
            fg = theme.fg_pose,
            bg = theme.bg_back,
            font = theme.fontThai_2,
            padx = 10)
        btn_back.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)


    def call_page_1():
        poseFull_2.grid_forget()
        poseFull_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_2():
        poseFull_1.grid_forget()
        poseFull_3.grid_forget()
        poseFull_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_3():
        poseFull_2.grid_forget()
        poseFull_4.grid_forget()
        poseFull_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_4():
        poseFull_3.grid_forget()
        poseFull_5.grid_forget()
        poseFull_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    def call_page_5():
        poseFull_4.grid_forget()
        poseFull_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# หน้าต่าง window หลัก
    window = Tk()
    window.title('ท่าออกกำลังกาย ทุกส่วน')
    window.configure(background = theme.background_color)

    img_1 = PhotoImage(master = window, file = "assets/full1.png") ## ใส่รูปภาพ
    poseFull_1 = Frame(window, bg = theme.bgcolor_detail)
    poseFull_1.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_2 = PhotoImage(master = window, file = "assets/full2.png") ## ใส่รูปภาพ
    poseFull_2 = Frame(window, bg = theme.bgcolor_detail)
    poseFull_2.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_3 = PhotoImage(master = window, file = "assets/full3.png") ## ใส่รูปภาพ
    poseFull_3 = Frame(window, bg = theme.bgcolor_detail)
    poseFull_3.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_4 = PhotoImage(master = window, file = "assets/full4.png") ## ใส่รูปภาพ
    poseFull_4 = Frame(window, bg = theme.bgcolor_detail)
    poseFull_4.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

    img_5 = PhotoImage(master = window, file = "assets/full5.png") ## ใส่รูปภาพ
    poseFull_5 = Frame(window, bg = theme.bgcolor_detail)
    poseFull_5.grid(row=0, column=0, padx=20, pady=10, sticky= (W, N, E, S))

# สร้างเนื้อหา/รายละเอียด ใน frames ทั้งหมด
    create_pose_1(img_1)
    create_pose_2(img_2)
    create_pose_3(img_3)
    create_pose_4(img_4)
    create_pose_5(img_5)

# ซ่อน frame ทั้งหมดไม่ให้แสดง ยกเว้นตามค่าของ check
    if check == 1:
        poseFull_2.grid_forget()
        poseFull_3.grid_forget()
        poseFull_4.grid_forget()
        poseFull_5.grid_forget()
    elif check == 2:
        poseFull_1.grid_forget()
        poseFull_3.grid_forget()
        poseFull_4.grid_forget()
        poseFull_5.grid_forget()
    elif check == 3:
        poseFull_1.grid_forget()
        poseFull_2.grid_forget()
        poseFull_4.grid_forget()
        poseFull_5.grid_forget()
    elif check == 4:
        poseFull_1.grid_forget()
        poseFull_2.grid_forget()
        poseFull_3.grid_forget()
        poseFull_5.grid_forget()
    else:
        poseFull_1.grid_forget()
        poseFull_2.grid_forget()
        poseFull_3.grid_forget()
        poseFull_4.grid_forget()


    mainloop()




##### แหล่งอ้างอิง

#    https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but?fbclid=IwAR1IZbI07mEhYGUp3P23eNwiyqneoF-auMWzmzHBO8C6CRiOiIs77-lVfKQ

#####
