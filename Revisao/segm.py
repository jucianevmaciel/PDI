import cv2
import numpy as np

# Carregar a imagem
caminho_imagem = "Revisao/moedas.jpeg"
imagem = cv2.imread(caminho_imagem, 1)

if imagem is None:
    print("Erro: Não foi possível carregar a imagem.")
else:
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro de suavização
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

    # Aplicar limiarização
    _, imagem_binaria = cv2.threshold(imagem_suavizada, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("", imagem_binaria)

    # Encontrar contornos
    contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar uma máscara para remover o contorno desejado
    mascara = np.ones(imagem.shape[:2], dtype="uint8")*255

    # Remover o contorno desejado
    for contorno in contornos:
        # Condição para identificar o contorno desejado
        if cv2.contourArea(contorno) > 500:  # Exemplo de condição
            cv2.findContours(mascara, [contorno], -1, 0, -1)

    # Aplicar a máscara na imagem original
    imagem_resultante = cv2.bitwise_and(imagem, imagem, mask=mascara)
    cv2.imshow("i", imagem_resultante)
    # Converter para escala de cinza novamente para a detecção de círculos
    imagem_cinza_resultante = cv2.cvtColor(imagem_resultante, cv2.COLOR_BGR2GRAY)

    # Aplicar filtro de suavização novamente
    imagem_suavizada_resultante = cv2.GaussianBlur(imagem_cinza_resultante, (15, 15), 0)

    # Detectar círculos usando a Transformada de Hough
    circulos = cv2.HoughCircles(imagem_suavizada_resultante, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                                param1=50, param2=30, minRadius=10, maxRadius=100)

    # Verificar se algum círculo foi detectado
    if circulos is not None:
        # Converter as coordenadas (x, y) e os raios dos círculos para inteiros
        circulos = np.round(circulos[0, :]).astype("int")

        # Desenhar os círculos detectados
        for (x, y, r) in circulos:
            cv2.circle(imagem_resultante, (x, y), r, (0, 255, 0), 4)  # Desenhar o círculo
            cv2.circle(imagem_resultante, (x - 5, y - 5), (x + 5, y + 5),r, (0, 188, 255), -1)  # Desenhar o círculo

           # cv2.rectangle(imagem_resultante, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)  # Desenhar o centro do círculo

    # Exibir a imagem com os círculos detectados
    cv2.imshow('Moedas Detectadas', imagem_resultante)

    # Exibir a imagem resultante
    cv2.imshow('Imagem Resultante', imagem_resultante)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
