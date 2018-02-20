from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MainView(App):
    def build(self):
        return Button(text='Hello World')



App = MainView()
App.run()

