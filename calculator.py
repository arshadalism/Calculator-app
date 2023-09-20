import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.geometry("644x1000")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    pass


scvalue = tkinter.StringVar()
scvalue.set("")
screen = tkinter.Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=tkinter.X, ipadx=8, padx=10, pady=45)
tkinter.Label(root, text="Calculator", font=("lucida 25  bold")).place(x=205, y=0)

f = tkinter.Frame(root, bg="grey", width=300, height=100)
b = tkinter.Button(f, text="9", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="8", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="7", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack(padx=100, pady=0)

f = tkinter.Frame(root, bg="grey")
b = tkinter.Button(f, text="6", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="5", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="4", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack(padx=100, pady=0)

f = tkinter.Frame(root, bg="grey")
b = tkinter.Button(f, text="3", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="2", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="1", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack(padx=100, pady=0)

f = tkinter.Frame(root, bg="grey")
b = tkinter.Button(f, text="0", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="-", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="*", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack(padx=100, pady=0)

f = tkinter.Frame(root, bg="grey")
b = tkinter.Button(f, text="/", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="+", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="=", padx=10, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=18, pady=2)
b.bind("<Button-1>", click)
f.pack(padx=100, pady=0)

f = tkinter.Frame(root, bg="grey")
b = tkinter.Button(f, text="C", padx=8, pady=3, font="lucida 30 bold")
b.pack(side=tkinter.LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="exit", padx=8, pady=3, font="lucida 30 bold", bg="red", command=root.quit)
b.pack(side=tkinter.LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = tkinter.Button(f, text="00", padx=8, pady=2, font="lucida 20 bold")
b.pack(side=tkinter.LEFT, padx=10, pady=0)
b.bind("<Button-1>", click)
f.pack(padx=80, pady=0)

root.mainloop()
