import TTS
import os, sys
import asyncio
import playsound
import random
import edge_tts as tts
import pandas as pd



voices_path = ('Voices.csv')

def play():
    text = input('Please enter the text you would like to speak: ')
    if text == 'exit':
        sys.exit()
    path = asyncio.run(TTS.record(text, 'title', tts_path)) #Record the Title, then the comments in TTS
    playsound.playsound(path, True)
    os.remove(path)
    play()

async def record(text, Title, path):
    VOICE = pd.read_csv(voices_path)
    VOICE = VOICE['Voice'].to_list()
    

    voice = random.choice(VOICE) #Uses a different voice per item (Title, comment, etc.)
    voices = await tts.VoicesManager.create()
    say = tts.Communicate(str(text), str(voice)) 
    say.stream

    save = path + '\\' + Title + '.mp3'
    
    await say.save(save)
    
    return save


if __name__ == '__main__':
    tts_path = ('Python\\TTS')
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(script_directory)
    play()
    

