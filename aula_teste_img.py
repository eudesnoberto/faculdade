import cv2
import os

# Função para coletar imagens de treinamento e atribuir rótulos
def coletar_imagens_e_rotulos(diretorio):
    imagens = []
    rotulos = []
    label = 0
    
    for subdiretorio in os.listdir(diretorio):
        subdiretorio_path = os.path.join(diretorio, subdiretorio)
        if os.path.isdir(subdiretorio_path):
            for imagem_nome in os.listdir(subdiretorio_path):
                imagem_path = os.path.join(subdiretorio_path, imagem_nome)
                imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
                imagens.append(imagem)
                rotulos.append(label)
            label += 1
            
    return imagens, rotulos

# Diretório contendo pastas de imagens de treinamento (uma pasta por pessoa)
diretorio_de_treinamento = "caminho/para/seu/diretorio/de/treinamento"

# Coletar imagens e rótulos de treinamento
imagens_treinamento, rotulos_treinamento = coletar_imagens_e_rotulos(diretorio_de_treinamento)

# Criar um modelo LBPH
modelo_lbph = cv2.face_LBPHFaceRecognizer.create()

# Treinar o modelo com as imagens e rótulos de treinamento
modelo_lbph.train(imagens_treinamento, np.array(rotulos_treinamento))

# Salvar o modelo em um arquivo XML
modelo_lbph.save("modelo_lbph.xml")

print("Treinamento concluído e modelo salvo.")
