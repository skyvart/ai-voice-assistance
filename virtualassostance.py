import pyttsx3 as py

vt=py.init()
rate=vt.getProperty('rate')
vt.setProperty('rate',180)

voices = vt.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
vt.setProperty('voice', voices[1].id)
def virtual(txt):
    print("speaking.......")
    vt.say(txt)
    vt.runAndWait()

txt="hello,i'am virtual assitance for pavan"
virtual(txt)

while txt!="bye":
    txt=input("say something:")
    txt=txt.lower()
    if txt!="bye":
        virtual(txt)
    else:
        print("virtual assistance:see you again, you call me at anytime")
        virtual("see you again pavan sir ,you can call me at anytime")
