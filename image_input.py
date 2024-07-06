import cv2
import os
import imutils
import requests
import numpy as np
DATA_DIR = './data'
url = "http://192.168.1.2:8080/shot.jpg"
def capture_image():
    counter,dataset_size = 0, 10
    while counter < dataset_size:
        img_resp = requests.get(url) 
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
        img = cv2.imdecode(img_arr, -1) 
        frame = imutils.resize(img, width=1000, height=1800)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR,'{}.jpg'.format(counter)), frame)
        counter += 1









    
