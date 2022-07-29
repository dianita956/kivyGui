#learning kivy
#date added July 29. 2022

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GridLayout(GridLayout):
    #initialize infinite keywords
    """docstring for ."""

    def __init__(self, **kwargs):
        #call gridlayoyt constructor
        super(GridLayout, self).__init__(**kwargs)
        #mapping columns and rows
        self.cols = 2

        #add widget
        self.add_widget(Label(text="Name: "))

        #add input box
        self.name = TextInput(multiline=False)


class MyApp(App):
    def build(self):
        return Label(text="hello world", font_size=72)


if __name__ == '__main__':
    MyApp().run()
