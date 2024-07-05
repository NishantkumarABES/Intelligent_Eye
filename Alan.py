import cv2
from voice_input import recognize_speech
from object_detection_model import detect_objects

from gtts import gTTS
import pygame
import io

def speak(text):
    sound = gTTS(text=text, lang='en')
    audio_data = io.BytesIO()
    sound.write_to_fp(audio_data)
    audio_data.seek(0)  
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


print("initiating Alan")
speak("initiating Alan")
#text = recognize_speech()
#print(text)


for i in range(10):
    path = r"data"+"\\"+str(i)+".jpg"
    print(path)
    img = cv2.imread(path)
    image, names = detect_objects(img)
    print(names)


cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
