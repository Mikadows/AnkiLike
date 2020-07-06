from pathlib import Path

from core.Data import Data
from tkinter import filedialog, messagebox

from core.services.SaveService import SaveService


class ImportService:

    def __init__(self):
        self.data = Data()

    def import_decks(self):
        file_path = filedialog.askopenfilename(title="Veuillez choisir un fichier JSON à importer",
                                               filetypes=[("JSON files", "*.json")])
        box = SaveService().get_json_box(Path(file_path))
        for deck in box.decks:
            self.data.box.add_deck(deck)
        messagebox.showinfo("Import", "Vos données ont été importées")