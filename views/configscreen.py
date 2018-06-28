from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from models.rootnode import RootNode
from views.mainscreen import MainScreen


class ConfigScreen(Screen):
    Builder.load_file("views/configscreen.kv")

    def start(self):
        r = RootNode(int(self.ids.node_count.text), int(self.ids.marker_count.text))
        self.manager.switch_to(MainScreen(r))
