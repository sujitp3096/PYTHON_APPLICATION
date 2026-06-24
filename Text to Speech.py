import pyttsx3

engine = pyttsx3.init()

text = input("Enter Text: ")

engine.say(text)
engine.runAndWait()
