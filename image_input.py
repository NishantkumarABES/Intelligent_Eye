import re
import os
import cv2
import imutils
import requests
import numpy as np
from PIL import ImageEnhance
from PIL import Image
from PIL import ImageFilter




DATA_DIR = './data'
dataset_size = 10
url = "http://192.168.1.2:8080/shot.jpg"
print('Collecting data')
done = False
while True:
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    frame = imutils.resize(img, width=1000, height=1800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

counter = 0
while counter < dataset_size:
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    frame = imutils.resize(img, width=1000, height=1800)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(DATA_DIR,'{}.jpg'.format(counter)), frame)
    counter += 1

cv2.destroyAllWindows()








    
