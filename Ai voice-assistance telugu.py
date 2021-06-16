import speech_recognition as sr
from gtts import gTTS
from playsound import playsound      
import os
import datetime as dt
import pywhatkit as pk

listener =sr.Recognizer()

def speak(cmd):
    print("Speaking........")
    print('')
    tts = gTTS(cmd,lang='te')
    tts.save('audio.mp3')
    playsound("audio.mp3")
    os.remove("audio.mp3")

va_name="జార్విస్ "
speak("నమస్కారం . నా పేరు జార్విస్ . మీకు ఎం సహాయం చేయాలి చెప్పండి ")
def take_cmd(check):
    command=""
    try:
      with sr.Microphone() as source:
           print("listening.......")
           print('')
           audio=listener.listen(source)
           if check:
                command=listener.recognize_google(audio,language="te")
                if va_name in command:
                  command=command.replace("జార్విస్  ","" )
                else:
                     command=""
           else:
                command=listener.recognize_google(audio,language="en-US")
            
    except:
        print("Check your Mic")
    return command
while True:
    final_cmd=take_cmd(True)
    if final_cmd!="":
        if "సమయం" in final_cmd:
            current_time= dt.datetime.now().strftime("%I:%M %p")
            speak(current_time)
        if "యూట్యూబ్" in final_cmd:
            speak("ఎమ్  వీడియో ప్లే  చేయాలి చెప్పండి ")
            final_cmd = take_cmd(False)
            pk.playonyt(final_cmd)
            print(final_cmd)
            print('')
            speak("ఆనందించండి . మీకు  అవసరం అయితే మల్లి  పిలవండి సర్")
            break
        if "గూగుల్" in final_cmd:
            speak("దేని  గురించి సెర్చ్ చేయాలో చెప్పండి ")
            final_cmd=take_cmd(False)
            print(final_cmd)
            print('')
            pk.search(final_cmd)

input("Press Enter to Exit")
            