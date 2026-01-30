from tkinter import *
from tkinter import messagebox
import string
import math

mainwindow = Tk()
mainwindow.geometry("400x400")
Label(mainwindow,text="Password Strength Checker",font=("Montserrat",18,"bold")).pack()
passwordentry = Entry(mainwindow)
passwordentry.pack()
def check_strength():
    global password
    password = passwordentry.get()
    N = 0
    length = len(password)
    for i in password:
        if i in string.digits:
            N+=len(string.digits)
            break
    for i in password:
        if i in string.ascii_lowercase:
            N+=len(string.ascii_lowercase)
            break
    for i in password:
        if i in string.ascii_uppercase:
            N+=len(string.ascii_uppercase)
            break
    for i in password:
        if i in string.punctuation:
            N+=len(string.punctuation)
            break

    entropy =math.log2(N**length)
    print (entropy)
    if entropy <= 72:
        messagebox.showinfo("Result","ts pretty weak gng")
    elif entropy <=115:
        messagebox.showinfo("Result","ts looks mid like u")
    elif entropy <= 200:
        messagebox.showinfo("Result","pretty strong ig")
    else:
        messagebox.showinfo("Result","ts so tuff fr")



checkbutton = Button(mainwindow,text="Check Strength",command=check_strength)
checkbutton.pack()



mainwindow.mainloop()