import cv2

# Caminho para o vídeo
video_path = 'ifma-480p.avi'

# Caminho para a imagem que você deseja sobrepor
imagem_path = 'logoif.png'

# Carregar o vídeo
video = cv2.VideoCapture(video_path)

# Carregar a imagem
imagem = cv2.imread(imagem_path)
scale_percent = 20 # percent of original size
width = int(imagem.shape[1] * scale_percent / 100)
height = int(imagem.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
imagem = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)



# Loop pelos frames do vídeo
while True:
    # Capturar o frame atual
    ret, frame = video.read()
    if not ret:
        break

    # Redimensionar a imagem para a mesma largura e altura do frame
    #imagem_redimensionada = cv2.resize(imagem, (frame.shape[1], frame.shape[0]))

    # Obter largura e altura da imagem
    (largura_imagem, altura_imagem) = imagem.shape[0:2]

    # Combinar o frame e a imagem
    resultado = frame.copy()
    resultado[0:largura_imagem, 0:altura_imagem] = imagem

    # Mostrar o resultado
    cv2.imshow('Video com imagem sobreposta', resultado)

    # Verificar se o usuário pressionou a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
video.release()
cv2.destroyAllWindows()
