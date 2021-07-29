import pandas as pd
import time, sys
from gtts import gTTS
import subprocess, time, sys
from rfid import parseRFID
import numpy as np


def showDetails(id, df):
    found = False
    for index, row in df.iterrows():
        if id == row['ID']:
            found = True
            sentence = " {} ".format(row['Name'])
            print(row['Name'])
            name = row['Name']
            if (not name or pd.isnull(name)):
                speak("No name stored in the record", language='en')
                print(sentence)
            elif row['Name']!= None :
                speak(sentence, language=row['Language'])
                break
                
    if found == False:
        sentence ="No ID found"
        speak(sentence, language='en')
        return False

def getLanguage(id, df):
    for index, row in df.iterrows():
        if id == row['ID']:
            return row['Language']
            break

def speak(sentence, language, slow = False):
    speech = gTTS(text = sentence, lang = language, slow = False)
    speech.save("text.mp3")
    subprocess.call(["mpg321", "text.mp3"])
 

if __name__ == '__main__':
    
    df = pd.read_excel(r'ExcelPanda1.xlsx', sheet_name='Sheet1')
    print(df)
    totalRows = len(df.index)
    while True:
        try:
            #id = input("enter an ID #:")
            id =parseRFID()
            print(id)
            if id.isnumeric():
                sentence = showDetails(int(id), df)
            else:
                print("Please enter a number")
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
    sys.exit()



