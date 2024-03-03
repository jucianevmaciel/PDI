import cv2
import numpy as np

imagem = cv2.imread('logo-if.jpg')

def ajuste_brilho(img, br):
    brilho = [br, br, br]
    res = np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.minimum(img[y, x] + brilho, [255, 255, 255])
    return res

def ajuste_contraste(img, cont):
    res = np.clip(img.astype(np.float32) * cont / 100, 0, 255).astype(np.uint8)
    return res

def efeito_negativo(img):
    return 255 - img

cv2.namedWindow('Brilho')
brilho = 0
result = imagem
contraste = 100

while True:
    cv2.imshow('Brilho', result)
    k = cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho = min(brilho + 50, 255)
        result = ajuste_brilho(imagem, brilho)
    elif k == ord('z'):
        brilho = max(brilho - 50, 0)
        result = ajuste_brilho(imagem, brilho)
    elif k == ord('n'):
        contraste = min(contraste + 50, 255)
        result = ajuste_contraste(imagem, contraste)
    elif k == ord('s'):
        contraste = max(contraste - 50, 0)
        result = ajuste_contraste(imagem, contraste)
    elif k == ord('b'):
        result = efeito_negativo(imagem)
    elif k == ord('c'):
        result = imagem

cv2.destroyAllWindows()
