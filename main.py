import speech_recognition as sr
from TTS.api import TTS
from pygame import mixer
import time

print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
tts = TTS('tts_models/en/ljspeech/tacotron2-DCA', gpu=False)
mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

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
        print(f"Could not request results: {e}")

    except sr.UnknownValueError:
        print("unknown error occurred")
