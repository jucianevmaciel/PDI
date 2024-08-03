import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
img = cv2.imread('Revisao/img.jpeg') 
imggau = cv2.medianBlur(img, ksize=3)
bordas=cv2.Canny(imggau,  100, 200)
gray = cv2.cvtColor(imggau, cv2.COLOR_BGR2GRAY) 
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 
contours, _ = cv2.findContours( 
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
  
i = 0
for contour in contours: 
  
    
    
    if i == 0: 
        i = 1
        continue
  
    
    approx = cv2.approxPolyDP( 
        contour, 0.1 * cv2.arcLength(contour, True), True) 
      
    
    cv2.drawContours(bordas, [contour], 0, (0, 0, 255), 3) 
  
    
    M = cv2.moments(contour) 
    if M['m00'] != 0.0: 
        x = int(M['m10']/M['m00']) 
        y = int(M['m01']/M['m00']) 
    else: x, y= 0, 0
    
    if len(approx) == 3: 
        cv2.putText(bordas, 'Triangle', (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
  
    elif len(approx) == 4: 
        cv2.putText(bordas, 'Quadrilateral', (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
  
    elif len(approx) == 5: 
        cv2.putText(bordas, 'Pentagon', (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
  
    elif len(approx) == 6: 
        cv2.putText(bordas, 'Hexagon', (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
  
    else: 
        cv2.putText(bordas, 'circle', (x, y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.1, (255, 255, 255), 2) 
cv2.imshow('shapes', bordas) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows()