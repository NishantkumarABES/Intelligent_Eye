from gtts import gTTS
import pygame
import io

def speak(text):
    print("\n" + text)
    sound = gTTS(text=text, lang='hi')
    audio_data = io.BytesIO()
    sound.write_to_fp(audio_data)
    audio_data.seek(0)  
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
