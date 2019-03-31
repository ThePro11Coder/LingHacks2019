import speech_recognition as sr
from PyDictionary import PyDictionary
from googletrans import Translator
import nltk 
from nltk.corpus import wordnet
import pyttsx3
engine = pyttsx3.init()
dictionary = PyDictionary()
translator = Translator()


def research():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Would you like to look for another word?")
        audio = r.listen(source)
    if r.recognize_google(audio) == "yes":
        print("I believe you said yes ok...")
        search_word()
    elif r.recognize_google(audio) == "no":
        print("Thanks for using the python Speech Dictionary")
    else:
        print("I couldn't understand what you said, please say something again")
        research()
        
def search_word():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Welcome to the voice recogniton dictionary")
        print("To find a word in the English Dictionary please say a word")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    speech = r.recognize_google(audio)
    try:
        print("Google Speech Recognition thinks you said " + speech)
    except sr.UnknownValueError:
        print("I couldn't understand what you said, please say something again")
        search_word()
    print(" ")
    print(dictionary.meaning(speech))
    synonyms = [] 
    antonyms = [] 
    for syn in wordnet.synsets(speech): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
  
    print("synonyms: ", set(synonyms))
    print(" ")
    print("antonyms: ", set(antonyms))
    print(" ")   
    translate(speech)
    research()

def translate(speech):
    print("To translate to spanish say 'span', for french say 'f', for italian say 'it', and if you don't want to translate say 'no' for none")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    if r.recognize_google(audio) == "span":
        speech_list=[speech]
        translations = translator.translate(speech_list, dest='es')
        for translation in translations:
            print(translation.origin, ' -> ', translation.text)
            engine.setProperty('rate', 150)    
            engine.setProperty('volume', 0.9)
            engine.say(translation.text)
            engine.runAndWait()
    elif r.recognize_google(audio) == "f":
        speech_list=[speech]
        translations = translator.translate(speech_list, dest='fr')
        for translation in translations:
            print(translation.origin, ' -> ', translation.text)
            engine.setProperty('rate', 150)    
            engine.setProperty('volume', 0.9)
            engine.say(translation.text)
            engine.runAndWait()
    elif r.recognize_google(audio) == "it":
        speech_list=[speech]
        translations = translator.translate(speech_list, dest='it')
        for translation in translations:
            print(translation.origin, ' -> ', translation.text)
            engine.setProperty('rate', 150)    
            engine.setProperty('volume', 0.9)
            engine.say(translation.text)
            engine.runAndWait()
    elif r.recognize_google(audio) == "no":
        print("Thanks for using the python Speech Dictionary")
        research()
    else:
        print("I couldn't understand what you said, please say one of the following options:")
        translate(speech)   
        

