#V.E.G.A. – Virtual Enhanced Guidance Assistant

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import sys

from openai import OpenAI


Recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="NA",  # your Perplexity API key
    base_url="https://api.perplexity.ai/"  # direct Perplexity endpoint
)

    response = client.chat.completions.create(
    model="sonar-pro",  
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Vega, skilled like Alexa or Google Assistant."},
        {"role": "user", "content": command}
    ],
    max_tokens=500
)

    return response.choices[0].message.content



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/") 

    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com") 

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__" :
    speak("Initializing Vega...")

    while True:
        print("Recognizing...")
        r = sr.Recognizer()

        # Better listening settings
        r.energy_threshold = 400  # sensitivity to sound
        r.dynamic_energy_threshold = True
        r.pause_threshold = 0.8   # pause between words handling

        #recognize speech
        try:
            with sr.Microphone() as s:
                print("Listening...")
                audio = r.listen(s, timeout=2, phrase_time_limit=1)
 
            word = r.recognize_google(audio)
            if(word.lower() == "vega"):
                engine.say("Listening")
              
                #listening command
                with sr.Microphone() as s:
                    print("Vega Active...")
                    audio = r.listen(s, timeout=5, phrase_time_limit=7)

                try:
                    command = r.recognize_google(audio)
                    print("You said:", command)
                    processCommand(command)

                     #Check if user wants to stop
                    if any(x in command.lower() for x in ["stop", "exit", "quit"]):
                        speak("Goodbye! Vega shutting down.")
                        sys.exit(0)

                    processCommand(command)


                except sr.UnknownValueError:
                    speak("Sorry, I didn’t catch that. Can you please say it again?")
               
                except sr.RequestError:
                    speak("Sorry, speech service is down right now.")

        except sr.UnknownValueError:
            # Didn’t catch the wake word
            pass

        except Exception as e:
            print("Error".format(e)) 
