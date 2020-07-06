from tkinter import filedialog

from core.Data import Data
from core.services.SaveService import SaveService


class ExportService:

    def __init__(self):
        self.data = Data()

    def export_box(self):
        file_path = filedialog.asksaveasfilename(title="Où enregistrer votre fichier ?",
                                               defaultextension='.json')

        SaveService().save_data(file_path, self.data)