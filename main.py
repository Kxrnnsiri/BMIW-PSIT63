from tkinter import *
import theme
from screen.workout import workoutSelector # อิมพอร์ตหน้าที่เราสร้างขึ้น

def main():
    def openWorkout():
        window.destroy() # close existing window before load new one
        workoutSelector()

    window = Tk()
    window.title('BMIW')
    window.geometry('480x320')
    window.configure(background = theme.background_color)

    # add button to load workout screen
    btn_workout = Button(
        window,
        text = 'Workout',
        command = openWorkout
    )

    btn_workout.pack()

    window.mainloop()

main()