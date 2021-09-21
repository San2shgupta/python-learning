
import wikipedia
import pyttsx3
while(True):
    result = input("enter topic\n")
    ret = result
    if result==ret:
         result = wikipedia.summary(result,sentences=2)
         print(result)
         speaker = pyttsx3.speak(result)
         continue

