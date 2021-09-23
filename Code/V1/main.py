import pyttsx3
import speech_recognition as sr
import pyaudio
import kivy
import nltk
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

def text_processing(query):
    print("starting processing")

class Grid_LayoutApp(App):
    def build(self):
        layout = GridLayout(rows=2, row_force_default=True, row_default_height=130)
        self.lb= Label(text="Welcome !",font_size="20sp",pos=(100, 250))
        self.btn = Button(text="Update Expense!",font_size="20sp",background_color=(1, 1, 1, 1),color=(1, 1, 1, 1),
                     size=(32, 32),size_hint=(.2, .2),pos=(300, 250))
        self.btn.bind(on_press=self.callback)
        layout.add_widget(self.lb)
        layout.add_widget(self.btn)


        return layout

    def callback(self, event):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        audio ="Hello I am AAPET !!"
        engine.say(audio)
        engine.runAndWait()
        audio = "Tell Me your Expenses"
        engine.say(audio)
        engine.runAndWait()



        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            self.lb.text=query
            print(query)
            text_processing(query)

        except Exception as e:
            print("say that again")
            self.lb.text="Say that again please"




root = Grid_LayoutApp()

root.run()





