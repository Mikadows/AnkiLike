from tkinter import filedialog

from core.Data import Data
from core.classes.Box import Box
from core.services.SaveService import SaveService


class ExportService:

    def __init__(self):
        self.data = Data()

    def export_box(self, box):
        file_path = filedialog.asksaveasfilename(title="Où enregistrer votre fichier ?",
                                               defaultextension='.json')

        SaveService().save_data(file_path, box)

    def export_selected_decks(self, list_check_decks):
        box = Box("AnkiLike", list())
        for i in range(len(list_check_decks)):
            if list_check_decks[i].get():
                box.add_deck(self.data.box.decks[i])
        self.export_box(box)
