import random

from kivy.event import EventDispatcher
from kivy.properties import NumericProperty
from models.marker import Marker


class ControlNode(EventDispatcher):
    marker_list = None
    id = NumericProperty()

    def __init__(self, child_count, id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marker_list = []
        self.id = id
        for x in range(child_count):
            self.marker_list.append(Marker())

    def randomize(self):
        markers_active = 2
        for m in self.marker_list:
            m.is_on = False
        numbers = random.sample(range(0, len(self.marker_list)), markers_active)
        for n in numbers:
            self.marker_list[n].is_on = True
