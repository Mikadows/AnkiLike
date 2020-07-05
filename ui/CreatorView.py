# coding:utf-8
import tkinter
import tkinter.font as tkFont


class CreatorView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()

        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.title = tkinter.Label(text="AnkiLike - Creator Mode", font=self.fontTitle)
        self.str_line = "_"*20
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.frame_menu = tkinter.LabelFrame(self.app, text="Deck management")
        self.create_deck = tkinter.Button(self.frame_menu, text="Create deck", command=self.load_create_deck_view)
        self.update_deck = tkinter.Button(self.frame_menu, text="Manage deck", command=self.load_deck_management_view)
        self.delete_deck = tkinter.Button(self.frame_menu, text="Delete deck", command=self.load_delete_deck_view)

        self.create_view()

    def create_view(self):
        self.title.pack()
        self.line.pack()
        self.frame_menu.pack(pady=20)
        self.create_deck.pack(padx=100, pady=10)
        self.update_deck.pack(padx=100, pady=10)
        self.delete_deck.pack(padx=100, pady=10)

    def load_deck_management_view(self):
        from ui.creatorviews.ManageDeck import ManageDeck
        ManageDeck(self.app)

    def load_create_deck_view(self):
        from ui.creatorviews.CreateDeck import CreateDeck
        CreateDeck(self.app)

    def load_delete_deck_view(self):
        from ui.creatorviews.DeleteDeck import DeleteDeck
        DeleteDeck(self.app)

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
