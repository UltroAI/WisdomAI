import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')

voices = engine.getProperty('voices')

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)



def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error.')
    return voice_text

if __name__ == '__main__':

    speak_text_cmd('Good part of the Day Mr. Sardor. How are you feeling today? ')

    while True:

        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('Hello Sir. How can i help you?')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\ {}'.format(voice_note.replace('Open ','')))
            continue
        elif 'bye' in voice_note:
            speak_text_cmd('See you next time Mr. Sardor. Have a nice time.')
            exit()
