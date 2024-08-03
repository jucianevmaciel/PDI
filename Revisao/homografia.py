import cv2
import numpy as np

# Ler as imagens
img1 = cv2.imread("Revisao/imagem1.jpeg")
img2 = cv2.imread("Revisao/imagem2.jpeg")

# Verificar se as imagens foram carregadas corretamente
if img1 is None or img2 is None:
    print("Erro ao carregar uma ou ambas as imagens.")
    exit()

# Converter para escala de cinza
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Criar o detector ORB
orb = cv2.ORB_create()

# Detectar e calcular descritores com ORB
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# Criar o matcher de descritores
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Encontrar correspondências
matches = bf.match(descriptors1, descriptors2)

# Ordenar as correspondências
matches = sorted(matches, key=lambda x: x.distance)

# Selecionar os melhores matches
num_matches = min(10, len(matches))  # Usar o mínimo entre 10 e o número total de matches
best_matches = matches[:num_matches]

# Extrair os pontos correspondentes
pts1 = np.float32([keypoints1[m.queryIdx].pt for m in best_matches]).reshape(-1, 1, 2)
pts2 = np.float32([keypoints2[m.trainIdx].pt for m in best_matches]).reshape(-1, 1, 2)

# Verificar se há pontos suficientes para calcular a homografia
if len(pts1) >= 4:
    # Calcular a matriz de homografia
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC)

    # Aplicar a transformação na imagem
    height, width, channels = img2.shape
    img1_transformed = cv2.warpPerspective(img1, H, (width, height))

    # Redimensionar a imagem 1 para ter a mesma altura que a imagem 2
    img1_resized = cv2.resize(img1, (width, height))

    # Criar uma imagem para desenhar as correspondências
    img_matches = cv2.hconcat([img1_resized, img2])

    # Desenhar as correspondências
    for m in best_matches:
        pt1 = keypoints1[m.queryIdx].pt
        pt2 = keypoints2[m.trainIdx].pt
        pt2 = (pt2[0] + img1_resized.shape[1], pt2[1])  # Ajustar para a posição concatenada

        cv2.line(img_matches, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])), (0, 255, 0), 2)

    # Mostrar a imagem com as correspondências
    cv2.imshow("Correspondências", img_matches)
    cv2.imshow("Imagem 1 Transformada", img1_transformed)
    cv2.imshow("Imagem 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Não há pontos suficientes para calcular a homografia.")
