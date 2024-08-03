import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("Revisao/img.jpeg", 1)


imggau = cv2.GaussianBlur(img, (5, 5), 0)
sobel = cv2.Sobel(imggau, -1,0 , 1)

(T, thresh)= cv2.threshold(imggau, 155, 255, cv2.THRESH_BINARY_INV)
kenel=np.ones((3,3), np.uint8)
sift = cv2.SIFT_create()
imgblur=cv2.medianBlur(img, 3)
bordas = cv2.Canny(imgblur, 100, 200)
erosao=cv2.morphologyEx(bordas,cv2.MORPH_CLOSE,kenel)
erosaoinv=cv2.erode(bordas, kenel)
circles = cv2.HoughCircles(bordas, cv2.HOUGH_GRADIENT,
                          dp=1.1,
                          minDist=300,
                          param1=200,
                          param2=40,
                          minRadius=50,
                          maxRadius=400)
print(circles)

circles = np.uint16(np.around(circles))
cimg = img.copy()
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(255,0,0),10)
    
keypoints, descriptors = sift.detectAndCompute(img, None)

imagem_com_pontos = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 8))

img=convert_bgr_to_rgb(img)
plt.subplot(231)
plt.imshow(img)
plt.title("imagem")

erosao=convert_bgr_to_rgb(erosao)
plt.subplot(232)
plt.imshow(erosao)
plt.title("erosao")

erosaoinv1=convert_bgr_to_rgb(erosaoinv)
plt.subplot(233)
plt.imshow(erosaoinv1)
plt.title("imagem")

cimg=convert_bgr_to_rgb(cimg)
plt.subplot(234)
plt.imshow(cimg)
plt.title("imagem")

sobel=convert_bgr_to_rgb(sobel)
plt.subplot(234)
plt.imshow(sobel)
plt.title("sobel")

plt.tight_layout()
plt.show()
#cv2.imshow("erosao", erosao)
#cv2.imshow("erosaoinv", erosaoinv)
#cv2.imshow("img", img)
#cv2.imshow("imggau", imgblur)
#cv2.imshow("imggau", bordas)
#cv2.imshow("imggau", cimg)
#cv2.imshow("", imagem_com_pontos)
#cv2.imshow("", thresh)

def convert_bgr_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_rgb = convert_bgr_to_rgb(img)
imgblur_rgb = convert_bgr_to_rgb(imgblur)
bordas_rgb = convert_bgr_to_rgb(bordas)
cimg_rgb = convert_bgr_to_rgb(cimg)
imagem_com_pontos_rgb = convert_bgr_to_rgb(imagem_com_pontos)

# Exibir imagens usando Matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(img_rgb)
plt.title("Imagem Original")

plt.subplot(232)
plt.imshow(imgblur_rgb)
plt.title("Imagem com Desfoque Mediano")

plt.subplot(233)
plt.imshow(bordas_rgb)
plt.title("Bordas Detectadas")

plt.subplot(234)
plt.imshow(cimg_rgb)
plt.title("Círculos Detectados")

plt.subplot(235)
plt.imshow(imagem_com_pontos_rgb)
plt.title("Pontos-chave SIFT")

plt.subplot(236)
plt.imshow(thresh, cmap='gray')
plt.title("Imagem Threshold")

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
