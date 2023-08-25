import cv2
import numpy as np

# Carregar a imagem em escala de cinza
image = cv2.imread('imgs\linda.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar a limiarização adaptativa
thres = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Salvar a imagem resultante
cv2.imwrite('imgs\imagem_desenho_detalhado.jpg', thres)

print("Imagem de desenho detalhado salva.")

