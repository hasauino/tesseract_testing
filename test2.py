#!/usr/bin/env python

import numpy as np
import cv2
import time
import pytesseract
from PIL import Image
cap = cv2.VideoCapture(0)



while True:
	print 'Capturing frame..'
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0,0), fx=.7, fy=.7) 
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	image = Image.fromarray(image)
        cv2.imshow('frame',frame)
        cv2.waitKey(1000)
        
	cv2.imwrite('messigray.png',frame)
	print 'Recognizing text..'
	#print pytesseract.image_to_string(image)
	'''
	time.sleep(5)
	'''

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

