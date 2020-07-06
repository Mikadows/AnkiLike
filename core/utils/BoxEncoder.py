import json
from json import JSONEncoder

from core.classes.Box import Box
from core.classes.Card import Card
from core.classes.Deck import Deck


class BoxEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Box, Deck, Card)):
            return vars(obj)
        else:
            return json.JSONEncoder.default(self, obj)
