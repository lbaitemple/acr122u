import subprocess, time, sys
from gtts import gTTS


def speak(sentence, language='en', slow =False):
    # search in the excel file to find name based on id in the excel file
    speech = gTTS(text = sentence, lang = language, slow = False)
    speech.save("text.mp3")
    subprocess.call(["afplay", "text.mp3"]) # on a mac book
    #subprocess.call(["mpg321", "text.mp3"]) # on a raspberry pi


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        try:
            sentence=input("enter a sentence #:")
            #language= https://cloud.google.com/speech-to-text/docs/languages
            speak(sentence, language='en')
            # do something time-cosnuming
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()

    sys.exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
