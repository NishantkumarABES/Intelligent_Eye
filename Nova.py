import cv2
from object_info import object_info
from voice_output import speak
from voice_input import recognize_speech
from object_detection_model import detect_objects
from image_input import capture_image

def image_analyzer():
    detected_objects = {}
    speak("Analyzing Captured Image")
    for i in range(10):
        path = r"data"+"\\"+str(i)+".jpg"
        img = cv2.imread(path)
        image, info = detect_objects(img)
        for name in info.keys():
            if name in detected_objects: continue
            else:
                if len(info[name])==1:
                    detected_objects[name] = 1
                else: detected_objects[name] = len(info[name]) 
    number = len(detected_objects)
    objects = list(detected_objects.keys())

    
    return number,objects,detected_objects,image


def responce_generator(number,objects,detected_objects):
    responce = f"{number} objects are recognized. Recognized objects are "
    for name in objects[:-1]:
        if detected_objects[name]==1:
            responce += "a "+name+","
        else: responce += str(detected_objects[name])+" "+name+","
    responce += "and "+(objects[-1] if detected_objects[objects[-1]]==1 else str(detected_objects[objects[-1]])+objects[-1])
    return responce


speak("Initiating Intelligent Eye")

while True:
    text = recognize_speech()
    if text == None: continue
    if text.lower() == "ok nova":
        speak("Hi, How can I help you sir!")
        activate = True
        break

words1 = ["capture","scan"]
words2 = ["explain","describe","identified","objects"]
words3 = ["display","image"]
words4 = ["describe","person"]
person = False
objects = None
image = None
while True:
    action = recognize_speech()
    if action == None: continue
    elif any(word.lower() in action.lower() for word in words1):
        speak("Sure Sir!")
        speak("Start Scanning")
        capture_image()
        speak("Scanning Complete")
        number,objects,detected_objects,image = image_analyzer()
        person = True if "person" in objects else False
        result = responce_generator(number,objects,detected_objects)
        speak(result)
    elif any(word.lower() in action.lower() for word in words3):
        if image==None: print("Image not found")
        cv2.imshow("Detected Objects", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif all(word.lower() in action.lower() for word in words4):
        if person:
            speak("please wait. Extract information.")
        else: print("No person found.")
    elif any(word.lower() in action.lower() for word in words2):
        if objects==None: print("No Object found.")
        speak("Sure Sir!")
        for item in objects: speak(item+". "+ object_info[item[0].upper()+item[1:]])
    
    elif "terminate" in action.lower():  
        speak("Thank you sir! Terminating Intelligent Eye")
        break



        





    






