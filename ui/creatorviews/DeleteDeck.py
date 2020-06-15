# coding:utf-8
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk

from ui.CreatorView import CreatorView


class DeleteDeck(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.create_view()

    def create_view(self):
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.title.pack()

        self.str_line = "_"*20
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.line.pack()


        self.frame_menu = tkinter.LabelFrame(self.app, text="Delete Deck")
        self.frame_menu.pack(pady=20)

        self.form_one = tkinter.Frame(self.frame_menu)
        self.form_one.pack()

        self.label_choose = tkinter.Label(self.form_one, text="Delete deck : ")
        self.label_choose.pack(side="left", pady=15, padx=30)

        self.tst = ttk.Combobox(self.form_one)
        self.tst.pack(pady=15, padx=5)

        self.delete_btn = tkinter.Button(self.frame_menu, text="Delete", command=self.delete)
        self.delete_btn.pack(pady=10)

        self.back_btn = tkinter.Button(self.frame_menu, text="Back", command=self.load_back_view)
        self.back_btn.pack(padx=100, pady=25)


    def delete(self):
        return

    def load_back_view(self):
        CreatorView(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
