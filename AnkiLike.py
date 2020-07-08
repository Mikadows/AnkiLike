# coding:utf-8
import tkinter
import sys
from pathlib import Path
from tkinter import messagebox

from core.Data import Data
from core.services.ExportService import ExportService
from core.services.ImportService import ImportService
from core.services.SaveService import SaveService
from core.utils.DataDummiesLoader import DataDummiesLoader
from ui.CreatorView import CreatorView
from ui.ExportView import ExportView
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
        self.a_menu.add_command(label="Import deck", command=self.import_decks)
        self.a_menu.add_command(label="Export deck", command=self.export_box)
        self.a_menu.add_separator()
        self.a_menu.add_command(label="Quit", command=on_closing)

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

    def import_decks(self):
        ImportService().import_decks()

    def export_box(self):
        #ExportService().export_box()
        ExportView(self.app)

def on_closing():
    confirm = messagebox.askyesnocancel("Quitter", "Sauvegarder avant de quitter ?", icon='warning')

    if confirm:
        Path('save').mkdir(parents=True, exist_ok=True)
        SaveService().save_data('save/save.json', data.box)
        root.destroy()
    elif confirm is None:
        pass
    else:
        root.destroy()

def on_saving(event):
    Path('save').mkdir(parents=True, exist_ok=True)
    SaveService().save_data('save/save.json', data.box)

if __name__ == "__main__":
    root = tkinter.Tk()

    data = Data()

    # load dummies random number of decks and cards
    if len(sys.argv) >= 2 and sys.argv[1] == "dataload":
        data.box = DataDummiesLoader().box_load()
    else:
        data.box = SaveService().get_json_box(Path("save/save.json"))
    app = AnkiLike(master=root)

    root.bind('<Control-s>', on_saving)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

