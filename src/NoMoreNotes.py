import speech_recognition as sr
import pyaudio, os, wave, time
import tqdm
import os.path
import datetime

filename = "audio.wav"
filepath = os.getcwd()

def main_menu():
    global filepath
    try:
        filename_output = str(input("What should this file be named? (Alphanumeric characters only please) "))
        filepath = filepath+"/"+filename_output+".html"
        date = datetime.datetime.today().strftime('%m/%d/%Y')

        f = open(filename_output+".html", "a")
        f.write("<center><u><h1>"+filename_output+"</h1></u><br><i>Note auto-generated by <a href='https://www.github.com/flancast90/NoMoreNotes'>NoMoreNotes</a> on "+date+"</i><br><br><p>")
        f.close()

        while True:
            record(filename_output)

    except KeyboardInterrupt:
        file_ = open(filename_output+".html", "a")
        file_.write("</p></center>")
        file_.close()

        os.rename(filename_output+".html", "../output/"+filename_output+".html")
        os.remove("audio.wav")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def speech_to_text(name):
    # initialize the recognizer
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        f = open(name+".html", "a")
        f.write(text+" ")
        f.close()


def record(name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "audio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

    frames = []

    cls()
    for i in tqdm.tqdm(range(0, int(RATE / CHUNK * RECORD_SECONDS))):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    speech_to_text(name)

main_menu()
