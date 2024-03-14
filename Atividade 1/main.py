import numpy as np
import cv2

img = cv2.imread("Atividade 1/colorred.jpg", 1)
img=img.shape(::2)
tamanho = 0.5
alt, larg, _ = img.shape
nAltura= int(alt*tamanho)
nLargura= int(larg*tamanho)

dim = (nLargura, nAltura)
novaimg=cv2.resize(img, dim, cv2.INTER_AREA)




hsv = cv2.cvtColor(novaimg, cv2.COLOR_BGR2HSV)
cinza = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
_, imagempb = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY_INV)
_, imagempbivn = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)


imagem_filtrada = cv2.(imagempbivn, (5, 5))
#imgred = cv2.cvtColor(imagempbivn, cv2.COLOR_GRAY2BGR)  
#imgred[np.where((imgred == [255, 255, 255]).all(axis=2))] = [0, 1, 255]


cv2.imshow("Imagem RGB", novaimg)
cv2.imshow("Imagem HSV", hsv)
cv2.imshow("Imagem PB", imagempb)
cv2.imshow("imagem red", imagem_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()
