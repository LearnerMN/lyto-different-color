import numpy as np
import cv2
import mss
from PIL import Image
from collections import defaultdict
        

monitor_number = 2

with mss.mss() as sct:
	monitor = sct.monitors[monitor_number]
	mon = {'top': monitor["top"] + 400, 'left': monitor["left"] + 120, 'width': 350, 'height': 400, 'mon': monitor_number}
	while True:
	    
	    img = np.array(sct.grab(mon))
	    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 10)
	    
	    if circles is not None:
	        circles = np.round(circles[0, :]).astype("int")
	        arr = []
	        for (x, y, r) in circles:
	            arr.append(list(img[y,x,:]))
	        	
	        color = max(arr,key=arr.count)
	        np_color = np.array(color)
	        mask = cv2.inRange(img, np_color, np_color)
	        img = cv2.bitwise_not(img, img, mask = mask)

	    cv2.imshow('Detect', np.array(img))
	    if cv2.waitKey(25) & 0xFF == ord('q'):
	        cv2.destroyAllWindows()
	        break