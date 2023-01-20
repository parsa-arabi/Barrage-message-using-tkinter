from tkinter import *
from tkinter import messagebox
from time import sleep
import keyboard
window = Tk()
window.title("Barrage Message")
window.geometry("400x500")
window.maxsize(400, 500)
window.minsize(400, 500)
window.configure(background="#A9A9A9")
photo = PhotoImage(file="icon.ico")
window.iconphoto(False, photo)

def start():
    get_1 = get1.get()
    get_2 = int(get2.get())
    if get_1 == "" or get_2 <= 0:
        messagebox.showinfo("Show info", "your text or selected number is very short!")
    if get_2 > 0 and get_1 != "":
        messagebox.showinfo("Show info", "start!Place your cursor on the Pia field and do not move it!")
        for i in range(get_2):
            keyboard.write(get_1)
            keyboard.press('enter')
            sleep(0.5)
        messagebox.showinfo("Show info", "success!")

Label(window, text="Barrage Message Program", background="#A9A9A9", font=('Tempus Sans ITC', 28)).pack()
Label(window, text="-----------------------------------------", background="#A9A9A9", font=('Tempus Sans ITC', 22)).pack()

window.configure(background="#A9A9A9")
Label(window, text="Enter your massage", bg="#A9A9A9", fg="black", font=('Tempus Sans ITC', 22)).pack()
Label(window, text="", background="#A9A9A9").pack()
get1 = Entry(window, font=('Tempus Sans ITC', 22), bg="#C0C0C0", bd=0)
get1.pack()
Label(window, text="-----------------------------------------", font=('Tempus Sans ITC', 22), bg="#A9A9A9").pack()

Label(window, text="Specify the number of messages", font=('Tempus Sans ITC', 22), bg="#A9A9A9", bd=0).pack()
get2 = Scale(window, from_=0, to=200, orient=HORIZONTAL, font=('Tempus Sans ITC', 22), bg="#A9A9A9", bd=0)
get2.pack(side='left', padx='40')
Button(window, text="start!", command=start, bd=0, font=('Tempus Sans ITC', 22), bg='#808080').pack(side='right', padx='40')
window.mainloop()
