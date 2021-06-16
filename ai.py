import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki


listener=sr.Recognizer()

speaker=pyttsx3.init()

rate=speaker.getProperty('rate')
speaker.setProperty('rate',160)

voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)

def speak(text):
    speaker.say("yes boss, "+text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

va_name="alexa"

speak("i am your"+va_name+", tell me boss")

def take_command():
    command = ''
    try:
         with sr.Microphone() as source:
            print("listening.........")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if va_name in command:
              command=command.replace(va_name+"","")
              
    except:
        print("check your microphone")
    return command

while True:
  user_command=take_command()
  if "close" in user_command:
      print("see you again sir . i will be there at anytime if you call me sir ")
      speak("see you again sir . i will be there at anytime if you call me sir ")
      break
  elif "what is time" in user_command:
      cur_time=dt.datetime.now().strftime("%I:%M %p")
      print(cur_time)
      speak(cur_time)
  elif "play" in user_command:
      user_command=user_command.replace("play ","")
      print("playing "+user_command)
      speak("playing "+user_command+",enjoy boss")
      pk.playonyt(user_command)
      break
  elif "hey google" in user_command or "google" in user_command:
      user_command=user_command.replace("hey google ","")
      user_command=user_command.replace("google ","")
      pk.search(user_command)
  elif "who is" in user_command:
      user_command=user_command.replace("who is","")
      info=wiki.summary(user_command,2)
      print(info)
      speak(info)
  elif "who are you " in user_command:
      speak_ex("i am your "+va_name+", tell me boss")
  else:
      speak_ex("please say it again boss")
