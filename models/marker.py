from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, NumericProperty


class Marker(EventDispatcher):
    is_on = BooleanProperty()
    id = NumericProperty()

    def __init__(self, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_on = False
        self.id = id

    def toggle(self):
        self.is_on = not self.is_on
