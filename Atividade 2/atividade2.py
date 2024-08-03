import cv2
# Variáveis globais para armazenar o estado do mouse e as coordenadas
desenho = False  # True quando o botão esquerdo do mouse é pressionado
ix, iy = -1, -1  # Coordenadas iniciais
pontos = []  # Lista para armazenar pontos desenhados

# Função de callback do mouse
def draw_circle(evento, x, y, flags, param):
    global ix, iy, desenho, pontos

    if evento == cv2.EVENT_LBUTTONDOWN:
        desenho = True
        ix, iy = x, y
        pontos.append((ix, iy))

    elif evento == cv2.EVENT_MOUSEMOVE:
        if desenho is True:
            cv2.line(frame, (ix, iy), (x, y), (0, 255, 0), 5)
            ix, iy = x, y
            pontos.append((ix, iy))

    elif evento == cv2.EVENT_LBUTTONUP:
        desenho = False
        cv2.line(frame, (ix, iy), (x, y), (0, 255, 0), 5)
        pontos.append((ix, iy))

capture = cv2.VideoCapture("Atividade 2/videos.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("LARGURA: '{}'".format(frame_width))
print("ALTURA: '{}'".format(frame_height))

if not capture.isOpened():
    print("Erro ao acessar câmera ou abrir o vídeo")
    exit()

addimagem = cv2.imread("Atividade 2/colorred.jpg")
addimagem = cv2.resize(addimagem, (99, 99))

gray = False

cv2.namedWindow('Vídeo')
cv2.setMouseCallback('Vídeo', draw_circle)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:

        ximg, yimg = 5, 4
        yimg1, yimg2 = yimg, yimg + addimagem.shape[0]
        ximg1, ximg2 = ximg, ximg + addimagem.shape[1]
        frame[yimg1:yimg2, ximg1:ximg2] = addimagem

        # Desenhar todos os pontos armazenados
        for i in range(1, len(pontos)):
            cv2.line(frame, pontos[i - 1], pontos[i], (0, 255, 0), 5)

        cv2.imshow('Vídeo', frame)

        if gray:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Cinza', gray_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            print("Salvando frame...")
            cv2.imwrite('print.jpg', frame)
        elif key == ord('b'):
            gray = not gray 
    else:
        break

capture.release()
cv2.destroyAllWindows()
