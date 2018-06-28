from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

from views.widgets.markerwidget import MarkerWidget


class ControlNodeWidget(StackLayout):
    Builder.load_file("views/widgets/controlnodewidget.kv")
    control_node = None

    def __init__(self, control_node, **kwargs):
        self.control_node = control_node
        super().__init__(**kwargs)
        Clock.schedule_once(self._after_init)

    def _after_init(self, *args):
        for m in self.control_node.marker_list:
            self.add_widget(MarkerWidget(m))
