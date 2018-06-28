from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from views.configscreen import ConfigScreen


class MarkerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ConfigScreen())
        return sm


if __name__ == '__main__':
    MarkerApp().run()
