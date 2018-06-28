from kivy.lang import Builder
from kivy.uix.button import Button


class MarkerWidget(Button):
    Builder.load_file("views/widgets/markerwidget.kv")
    marker = None

    def __init__(self, marker, **kwargs):
        self.marker = marker
        super().__init__(**kwargs)
