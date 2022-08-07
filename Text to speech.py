#Project on text to speech conversion
import pyttsx3
engine=pyttsx3.init()
engine.say("Hey I can speeak now. What you want to speak from me.")
engine.runAndWait()
while True:
    engine.say("write your text: ")
    engine.runAndWait()
    text=input("write here: ")
    engine.say(text)
    engine.runAndWait()
    engine.say("Do you want to continue?")
    engine.runAndWait()
    ans=input("Do you want to continue:")
    if(ans!="yes"):
        break;
engine.runAndWait()