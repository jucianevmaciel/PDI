#Faça a redução da resolução de uma imagem tomando 
#por base a media dos pixels da vizinhança-8.

#▪Faça a redução da resolução de uma imagem tomando
#por base a eliminação dos pixels na vizinhança-8.

import cv2
import numpy as np

img = cv2.imread('Atividade 4/logo-if.jpg')
def resol (var):
    resolucao=np.hstack([cv2.blur(img, (var,var))])
    return resolucao

def resol1(var):
    resolucao1=img[::var, ::var]
    return resolucao1


result = img
var=1
while True:
    cv2.imshow("Imagens ", result)
    k = cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('s'):
       var+=1
       result= resol(var)
    elif k == ord('d'):
       var+=1
       result= resol1(var)
    
cv2.waitKey(0)
