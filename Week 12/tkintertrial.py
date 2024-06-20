#! python3
#       learning tkinter to make a gui for a calculator

from tkinter import *
from tkinter import messagebox
import random

# ------------------------------------ Random Int + Window ------------------------------ #

mynumber = random.randint(1, 10)
print(mynumber)


# window variable
window = Tk()
# our title
window.title('R4inssss TK demo')
# w x h for window size (like pygame)
window.geometry('500x400')


# ------------------------------------ Windows Callable ------------------------------ #

def btnOk_clicked():
    guess = int(spinNumber.get())
    if guess == mynumber:
        messagebox.showinfo(title='Congratulations!', message='You guessed the right number!')
    else:
        messagebox.showinfo(title='Wrong!', message='You guessed the wrong number!')


def btnCancel_clicked():
    window.destroy()


# ------------------------------------ Widgets ------------------------------ #

lbl = Label(window, text='Hello World')
lbl.grid(column=0, row=0)

# Spinbox
txt_spin_value = 1
spinNumber = Spinbox(window, from_=1, to=10, width=5, textvariable=txt_spin_value)
spinNumber.grid(column=1, row=0)

# Buttons
btnOk = Button(window, text='Ok', command=btnOk_clicked)
btnOk.grid(column=0, row=2)

btnCancel = Button(window, text='Cancel', command=btnCancel_clicked)
btnCancel.grid(column=1, row=2)

window.mainloop()
