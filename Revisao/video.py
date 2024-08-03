import cv2
import numpy as np

capture = cv2.VideoCapture("Atividade 2/videos.mp4")


if not capture.isOpened():
    print("Erro ao acessar câmera ou abrir o vídeo")
    exit()

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        sift = cv2.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(frame, None)

# Desenhar os pontos de interesse
        imagem_com_pontos = cv2.drawKeypoints(frame, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow("1", imagem_com_pontos)
        vedio=cv2.medianBlur(frame, 5)
        cv2.imshow('Vídeo', vedio)  
        bordas = cv2.Canny(frame, 100, 200)
        #cv2.imshow('Vídeo', bordas)  

        circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT,
                                dp=1.1,
                                minDist=300,
                                param1=200,
                                param2=40,
                                minRadius=90,
                                maxRadius=700)
        print(circles)

        circles = np.uint16(np.around(circles))
        cimg = frame.copy()
        for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(frame,(i[0],i[1]),15,(255,0,0),10)
                
                keypoints, descriptors = sift.detectAndCompute(frame, None)

                imagem_com_pontos = cv2.drawKeypoints(frame, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break  
        elif key == ord('w'):
            print("Salvando frame...")
            cv2.imwrite('print.jpg', frame)  
    else:
        break  
capture.release()
cv2.destroyAllWindows() 