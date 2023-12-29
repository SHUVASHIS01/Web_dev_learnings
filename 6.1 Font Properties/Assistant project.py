import speech_recognition as sr
Listener= sr.Recognizer()
try:
    with sr.Microphone as source:
        print('Listening....')
        voice=Listener.listen(source)
        command=Listener.recognize_google(voice)
        print(command)
except:
    pass