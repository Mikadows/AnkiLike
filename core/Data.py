from core.classes.Box import Box
from core.utils.Singleton import Singleton


class Data(Singleton):
    def __init__(self):
        self._box = None
    def _get_box(self):
        return self._box
    def _set_box(self, box):
        self._box = box
    box = property(_get_box, _set_box)
