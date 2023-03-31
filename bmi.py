import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.title("BMI 계산기")

window.resizable(False, False)

window.geometry("640x400+300+300")

he = tkinter.StringVar()
we = tkinter.StringVar()
def btn_click() :
    h = float(he.get())
    w = float(we.get())
    h = h * 0.01
    mesg = he.get()
    result = w / (h*h) 
    tkinter.messagebox.showinfo("결과",result)

label=tkinter.Label(window, text="BMI 계산기")
label.config(font=("Arial",25))
label.config(fg="red")
label.pack()

heightLabel = tkinter.Label(window, text="신장")
heightLabel.config(font=("Arial", 24))
heightLabel.place(x=30, y=70)

heightEntry = tkinter.Entry(window, textvariable=he)
heightEntry.place(x=120, y=82)

heightLabel = tkinter.Label(window, text="체중")
heightLabel.config(font=("Arial", 24))
heightLabel.place(x=30, y=120)

heightEntry = tkinter.Entry(window, textvariable=we)
heightEntry.place(x=120, y=130)

btn = tkinter.Button(window, text="제출",command=btn_click)
btn.place(x=120, y = 250)

button.pack()


window.mainloop()

