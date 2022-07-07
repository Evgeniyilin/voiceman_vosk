#!/usr/bin/env python3
import time
import pyperclip


from vosk import Model, KaldiRecognizer
import os, json

import playsound

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

import pyaudio

import difflib
def similarity(s1, s2):  
  matcher = difflib.SequenceMatcher(None, s1, s2)
  return matcher.ratio()
genuine = (
    "",
    "гет запрос",
    "пост запрос",
    "крит реакт эп",
    "крит дата бэйс",
)

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()

while True:
    CurrentTime = time.time()    
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x=json.loads(rec.Result())        
        if x["text"] == "ассистент":
            stream.stop_stream()
            pyperclip.copy('')
            CurrentTime = time.time()
            print(x["text"])
            playsound.playsound("start.mp3", block = False)
            stream.start_stream()
            while (int(round(time.time() - CurrentTime))) <= 4:
                data = stream.read(4000, exception_on_overflow=False)
                if rec.AcceptWaveform(data):
                    x=json.loads(rec.Result())

                    per_match = similarity(genuine[0], x["text"])    
                    i = 0
                    id = 0
                    while i < len(genuine):
                        if (per_match < similarity(genuine[i], x["text"])):
                            per_match = similarity(genuine[i], x["text"])
                            id = i
                        i += 1
                    if per_match > 0.5:
                        put = f'lib/{id}.txt'
                        f = open(put, 'r', encoding="utf-8")
                        pyperclip.copy(f.read())
                    
                    print(id, per_match)

                    if x["text"] == "ассистент":
                        print(x["text"])
                        pyperclip.copy('hello world!')



            playsound.playsound("stop.mp3", block = False)            

    # print("new_iteration")

print(rec.FinalResult())
