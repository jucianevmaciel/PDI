import cv2
import numpy as np
capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("Avaliacao1/ifma-480p.avi")
img = cv2.imread("Avaliacao1/logoif.png",)
cv2.imshow("a", img)

ret, frame = capture.read()

rows, cols, c= img.shape
logo = frame[0:rows, 0:cols]

img1 =img.copy()
img1[0:rows, 0:cols] = img
frame("", img1)



if not capture.isOpened():
    print("Erro ao acessar camera ou abrir o vídeo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            cv2.imshow('Input', frame)
            #cv2.imshow("Avaliacao1/logoif.png", 1)
         
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg',frame)
                
        else: break

capture.release()
cv2.destroyAllWindows()