from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#to create executable
import os, sys
from kivy.resources import resource_add_path

class BackupApp(App):
    def build(self):
        self.title = "Simple Backup Solition"
        return Builder.load_file(self.resource_path('my.kv'))

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')
        return os.path.join(base_path, relative_path)

Window.size = (500, 700)
Builder.load_file('my.kv')
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Hatalı bir giriş yaptınız." in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"


    def esitlik(self):
        try:
            prior = self.ids.calc_input.text
            cevap = int(eval(prior))
            self.ids.calc_input.text = f"{cevap}"
        except:
            self.ids.calc_input.text = "Hatalı bir giriş yaptınız."

    def noktaylaayirma(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    def silme(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def artieksi(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

class MyApp(App):
    def build(self):
        Window.clearcolor=(186/255, 184/255, 184/255, 1)
        return MyLayout()
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(( os.path.join(sys._MEIPASS)))
    MyApp().run()