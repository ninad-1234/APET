import pyttsx3
import speech_recognition as sr
import pyaudio
import kivy
import nltk
from nltk.corpus import stopwords
from firebase import firebase
from nltk.tokenize import RegexpTokenizer
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from nltk.corpus import wordnet as wn

firebase = firebase.FirebaseApplication("https://apet-2001-default-rtdb.asia-southeast1.firebasedatabase.app",None)


def fire_base_connect(category,num):

    data= {
        'category': category,
        'cost': num
    }
    result= firebase.post('/apet-2001-default-rtdb/user',data)

def text_processing(query):
    print("starting processing")
    print(query)
    li = list(query.split(" "))
    print(li)

    stop_words = set(stopwords.words('english'))

    removing_stop_word = []
    numeric_data=[]
    for i in li:
        if (i not in stop_words):
            if(i.isnumeric()):
                numeric_data.append(i)
            else:
                removing_stop_word.append(i)

    print(removing_stop_word)
    print(numeric_data)
    food=["eat","dish","hotel"]
    Medical=["doctor","medicine","clinic"]
    category=""
    for i in removing_stop_word:
        i=i.lower()
        if(i in food):
            category= "Food"
        elif (i in Medical):
            category= "Medical"
    print(category)
    fire_base_connect(category,numeric_data[0])
    return category


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
            cat=text_processing(query)
            self.lb.text="Expense Category :-  "+cat

        except Exception as e:
            print("say that again")
            self.lb.text="Say that again please"




root = Grid_LayoutApp()

root.run()





