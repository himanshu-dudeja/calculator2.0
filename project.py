from mathy import *
import speech_recognition as sr

"""Below variable is used to end the loop whenever required
Using Google speech recognition so it will work only with active interet connection"""

x = 1
while x == 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please input your voice, I am Listening")
        audio = r.listen(source)
        print("Processing your input")
    try:
        text = ("YOUR INTERPRETED INPUT: "+r.recognize_google(audio))
        print(text)
        for word in text.split(" "):
            if word.upper() in operations.keys():
                try:
                    l = extract_numbers_from_text(text)
                    r = operations[word.upper()](l[0], l[1])
                    print(r)
                except:
                    print("Unable to process")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                x = 0
                break
        else:
            sorry()
    except:
        pass
