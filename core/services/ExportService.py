from tkinter import filedialog

from core.Data import Data
from core.classes.Box import Box
from core.services.SaveService import SaveService

import copy

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
                box.add_deck(copy.deepcopy(self.data.box.decks[i]))
        self.reset_validation_levels(box)
        self.export_box(box)

    def reset_validation_levels(self, box):
        for deck in box.decks:
            for card in deck.cards:
                card.validation_level = 0
