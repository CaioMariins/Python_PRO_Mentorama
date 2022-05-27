from kivy.app import App
from kivy.uix.widget import Widget

class Telinha(Widget):
    pass


class Example(App):
    def build(self):
        return Telinha()


if __name__ == '__main__':
    Example().run()