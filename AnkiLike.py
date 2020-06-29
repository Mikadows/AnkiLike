# coding:utf-8
import tkinter

from core.Data import Data
from core.utils.DataDummiesLoader import DataDummiesLoader
from ui.CreatorView import CreatorView
from ui.PlayerView import PlayerView


class AnkiLike(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.pack()
        self.create_main_view()

    def create_main_view(self):
        self.app.minsize(720, 480)
        self.app.title("AnkiLike")

        self.mainmenu = tkinter.Menu(self.app)

        self.a_menu = tkinter.Menu(self.mainmenu, tearoff=0)
        self.a_menu.add_command(label="Import deck")
        self.a_menu.add_command(label="Export deck")
        self.a_menu.add_separator()
        self.a_menu.add_command(label="Quit", command=self.app.quit)

        self.m_modes = tkinter.Menu(self.mainmenu, tearoff=0)
        self.m_modes.add_command(label="Player Mode", command=self.load_player_view)
        self.m_modes.add_command(label="Creator Mode", command=self.load_creator_view)

        self.mainmenu.add_cascade(label="AnkiLike", menu=self.a_menu)
        self.mainmenu.add_cascade(label="Modes", menu=self.m_modes)
        self.app.config(menu=self.mainmenu)

        self.load_player_view()

    def load_player_view(self):
        PlayerView(self.app)

    def load_creator_view(self):
        CreatorView(self.app)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = AnkiLike(master=root)
    data = Data()
    data.box = DataDummiesLoader().box_load()
    print(len(data.box.decks))
    dataCheck = Data()

    print(len(dataCheck.box.decks))
    app.mainloop()
