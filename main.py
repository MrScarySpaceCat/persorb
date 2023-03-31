import speech_recognition as sr
import pyttsx3
from TTS.api import TTS
from pygame import mixer
import os
import time

print(sr.Microphone.list_microphone_names())

# Initialize the recognizer
r = sr.Recognizer()

# initialize class to convert text to speech
tts = TTS('tts_models/en/ljspeech/tacotron2-DCA', gpu=False)

# initialize the mixer
mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")


# Loop infinitely for user to speak

while True:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_whisper(audio2, language="english")
            MyText = MyText.lower()

            print("You said:", MyText)
            try:
                tts.tts_to_file(text=MyText, file_path='temp.wav')
            except ValueError:
                pass

            mixer.music.load('temp.wav')
            mixer.music.play()
            mixer.music.set_volume(25.0)
            while mixer.music.get_busy():
                time.sleep(0.1)
            else:
                mixer.music.unload()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
