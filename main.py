from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TruvaAtiApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="BASIT HESAP MAKINESI", font_size=30)
        self.layout.add_widget(self.label)

        self.input1 = TextInput(hint_text="Birinci sayi", multiline=False, input_filter='int')
        self.layout.add_widget(self.input1)

        self.input2 = TextInput(hint_text="Ikinci sayi", multiline=False, input_filter='int')
        self.layout.add_widget(self.input2)

        self.btn = Button(text="HESAPLA", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.kontrol)
        self.layout.add_widget(self.btn)

        return self.layout

    def kontrol(self, instance):
        # Senin telefon numaranin son 4 hanesi ve ilk 2 hanesi sifre!
        if self.input1.text == "1972" and self.input2.text == "55":
            self.siber_panel()
        else:
            self.label.text = "Sonuc: " + str(int(self.input1.text or 0) + int(self.input2.text or 0))

    def siber_panel(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text="🕵️ HISOKA SIBER PANEL 🕵️", font_size=35, color=(1, 0, 0, 1)))
        
        # Proje 1
        self.layout.add_widget(Button(text="Akilli 'Hangi Filmi İzlesem?'", size_hint_y=None, height=100))
        # Proje 2
        self.layout.add_widget(Button(text="Boy-Kilo ve Form Olcer", size_hint_y=None, height=100))
        
        self.layout.add_widget(Label(text="Sistem Aktif: İlkbey", font_size=15))

if __name__ == '__main__':
    TruvaAtiApp().run()
  
