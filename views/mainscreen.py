from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from views.widgets.controlnodewidget import ControlNodeWidget


class MainScreen(Screen):
    Builder.load_file("views/mainscreen.kv")

    root_node = None

    def __init__(self, root_node, **kw):
        super().__init__(**kw)
        self.root_node = root_node
        Clock.schedule_once(self._after_init)

    def _after_init(self, *args):
        for n in self.root_node.nodes:
            self.ids.nodes_container.add_widget(ControlNodeWidget(n))
