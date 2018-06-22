import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("600x400")

var = tk.StringVar()
var.set("Hello python!")

label_1 = tk.Label(window,
                   textvariable=var,
                   bg="greenyellow",
                   font=("Courier New", 18),
                   width=15, height=1)

label_1.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit is False:
        on_hit = True
        var.set("You hit me")
    else:
        on_hit = False
        var.set("Hello python!")


button = tk.Button(window, text="hit me",
                   width=15, height=1,
                   command=hit_me)

button.pack()

window.mainloop()
