#Faça a redução da resolução de uma imagem tomando 
#por base a media dos pixels da vizinhança-8.

#▪Faça a redução da resolução de uma imagem tomando
#por base a eliminação dos pixels na vizinhança-8.

import cv2
import numpy as np

img = cv2.imread('Atividade 4/logo-if.jpg')
img2=cv2.imread('Revisao/img.jpeg')

img2=cv2.resize(img2,(119,99), interpolation=cv2.INTER_AREA)
linhas,colunas, channels=img2.shape
techo=img[0:linhas, 0:colunas]
x, y = 50, 50 
if y + linhas <= img.shape[0] and x + colunas <= img.shape[1]:
    # Definir a região de interesse (ROI) em img
    roi = img[y:y+linhas, x:x+colunas]

    # Substituir a ROI com img2
    img[y:y+linhas, x:x+colunas] = img2
cv2.imshow("",img)
mask = np.zeros(img.shape[:2], np.uint8)
center_coordinates = (15, 20)  # exemplo de coordenadas do centro da bola
radius = 20  # exemplo de raio da bola
cv2.circle(mask, center_coordinates, radius, 255, -1)
imgin =cv2.inpaint(img, mask, 15, cv2.INPAINT_TELEA)
cv2.imshow("img1", imgin)


def resol (var):
    resolucao=np.hstack([cv2.blur(img, (var,var))])
    return resolucao

def resol1(var): 
    resolucao1=img[::var, ::var]
    return resolucao1


result = img
var=1
#while True:
    #cv2.imshow("Imagens ", result)
    #k = cv2.waitKey(20)
    #if k == ord('a'):
     #   break
    #elif k == ord('s'):
     #  var+=1
      # result= resol(var)
    #elif k == ord('d'):
     #  var+=1
      # result= resol1(var)
    
cv2.waitKey(0)
