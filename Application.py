#coding:utf-8
import tkinter

# Creating main frame
app = tkinter.Tk()
app.minsize(720, 480)
app.title("AnkiLike")

mainmenu = tkinter.Menu(app)

f_menu = tkinter.Menu(mainmenu)
f_menu.add_command(label="Player Mode")
f_menu.add_command(label="Creator Mode")

mainmenu.add_cascade(label="AnkiLike - Modes", menu=f_menu)


# Principal loop
app.config(menu=mainmenu)
app.mainloop()

