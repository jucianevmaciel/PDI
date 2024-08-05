import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("Revisao/imgem.jpg", 1)


kernel = np.array([[0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0]], np.uint8)

#filtered_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
erosion = cv2.erode(img, kernel, iterations=5)

#cv2.imshow("Filtro Personalizado", filtered_img)
cv2.imshow("Filtro Personalizado", erosion)
plt.figure(figsize=(12, 8))


plt.subplot(231)
plt.imshow(img)
plt.title("imagem")

plt.subplot(232)
plt.imshow(erosion)
plt.title("imagem")
plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()