# coding:utf-8
import tkinter
import tkinter.font as tkFont
from core.Data import Data
from core.services.ExportService import ExportService


class ExportView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.app = master
        self.clear()
        self.data = Data()

        self.str_line = "_" * 20
        self.fontTitle = tkFont.Font(family="Lucida Grande", size=20)
        self.line = tkinter.Label(text=self.str_line, font=self.fontTitle)
        self.title = tkinter.Label(text="AnkiLike - Export Mode", font=self.fontTitle)
        self.label_frame = tkinter.LabelFrame(self.app, text="Choisissez les decks à exporter")
        self.list_check_decks = list()

        self.export_deck_button = tkinter.Button(text="Exporter les decks sélectionnés", command=self.export_decks)
        self.export_all_decks_button = tkinter.Button(text="Exporter tous les decks", command=self.export_all_decks)
        self.create_view()

    def export_decks(self):
        ExportService().export_selected_decks(self.list_check_decks)

    def export_all_decks(self):
        [value.set(True) for value in self.list_check_decks]
        ExportService().export_selected_decks(self.list_check_decks)

    def create_view(self):
        self.title.pack()
        self.line.pack()

        if self.data.box.decks is not None:
            for i in range(len(self.data.box.decks)):
                self.list_check_decks.append(tkinter.IntVar())
                tkinter.Checkbutton(self.label_frame,
                                    text=self.data.box.decks[i].name,
                                    variable=self.list_check_decks[i]).pack()
        self.label_frame.pack(pady=20)
        self.export_deck_button.pack()
        self.export_all_decks_button.pack()

    def clear(self):
        for widget in self.app.winfo_children():
            widget.pack_forget()
