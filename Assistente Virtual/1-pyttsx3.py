# pip install pyttsx3==2.71  // vamos usar essa versão especifica que é estavel
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice","")
engine.say("Hello World. Language Python")
#engine.say("Olá mundo, vamos transformar texto em voz")
engine.runAndWait()
