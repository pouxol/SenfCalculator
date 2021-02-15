from tkinter import *


def button_clicked():
    num = int(input.get())
    num_ml = round(num / 1.08, 2)
    output.config(text=num_ml)


window = Tk()
window.title("Worlds first Senf Unit Converter")
window.minsize(width=350, height=200)
window.config(padx=30, pady=20)

title = Label(text="Senf", font=("Arial", 24, "bold"))
title.grid(row=0, column=1)
title.config(padx=5, pady=5)

gram = Label(text="gram", font=("Arial", 12))
gram.grid(row=1, column=2)
gram.config(padx=5, pady=5)

equal = Label(text="is equal to", font=("Arial", 12))
equal.grid(row=2, column=0)
equal.config(padx=5, pady=5)

ml = Label(text="ml", font=("Arial", 12))
ml.grid(row=2, column=2)
ml.config(padx=5, pady=5)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=1)
button.config(padx=5, pady=5)

output = Label(text=0, font=("Arial", 12, "bold"))
output.grid(row=2, column=1)
output.config(padx=5, pady=5)


input = Entry(width=20)
input.grid(row=1, column=1)
input.get()

window.mainloop()
