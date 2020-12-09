from tkinter import*
from tkinter import messagebox
def profile():
    profile = Tk()
    profile.geometry("600x430")
    profile.configure(background='#660000')
    profile.title("BMIW")
    bmiw = PhotoImage(file="Header.png")
    Label(profile, image=bmiw,borderwidth=0).pack(side=TOP,pady=0)
    Label(profile, text="Username",font ="Mali 12", bg="#660000",fg = "#FFFFFF").pack(side=TOP,pady=0,padx=10)
    name = Entry(profile, font="consolas 15", bg="#FFFFFF",fg="#660000")
    name.pack(side=TOP,pady=0,padx=60)
    name1 = name.get()
    Label(profile, text="Password" , font="Mali 12", bg="#660000", fg="#FFFFFF").pack(side=TOP, pady=0, padx=10)
    password = Entry(profile, font="consolas 15", bg="#FFFFFF",fg="#660000")
    password.pack()
    password1=password.get()



    def check():
        name1 = name.get()
        password1 = password.get()
        if name1 == "bmiw" and password1 == "1234":
            profile.destroy()
            return name1 and password1
        else:
            messagebox.showerror("Error!!!!"," This name can't be use ")


    end = Button(profile, text="Login",bg="#FFFFFF",fg="#660000",font ="Mali 8",command=check).pack(side=TOP,pady=20,ipady=0)
    Label(profile, text=" By PROTHON",font="Mali 10",fg="#FFFFFF",bg="#660000").pack(side=RIGHT, padx=10)
    profile.mainloop()

profile()

