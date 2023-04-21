from kivy.app import App
#az app modul tartalmazza az App osztályt
from kivy.uix.widget import Widget
#kivi mappából az uix mappa

class TesztApp(App):
    def build(self):
        return Widget()

TesztApp().run()