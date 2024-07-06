import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print()
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)
        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"Nova thinks you said: {text}")
            return text
        except sr.UnknownValueError:
            print("Nova could not understand audio")
        except sr.RequestError as e:
            print(f"Request Error; {e}")
        return None

if __name__ == "__main__":
    recognize_speech()
