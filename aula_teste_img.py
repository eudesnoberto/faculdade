import cv2
import face_recognition

# Carregar imagens de treinamento
imagem_pessoa1 = face_recognition.load_image_file("caminho/para/pessoa1.jpg")
imagem_pessoa2 = face_recognition.load_image_file("caminho/para/pessoa2.jpg")

# Extrair codificações de rostos das imagens de treinamento
codificacao_pessoa1 = face_recognition.face_encodings(imagem_pessoa1)[0]
codificacao_pessoa2 = face_recognition.face_encodings(imagem_pessoa2)[0]

# Criar listas de codificações e nomes conhecidos
codificacoes_conhecidas = [codificacao_pessoa1, codificacao_pessoa2]
nomes_conhecidos = ["Pessoa1", "Pessoa2"]

# Inicializar a webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capturar um frame
    ret, frame = video_capture.read()

    # Encontrar todas as faces no frame
    face_locations = face_recognition.face_locations(frame)
    codificacoes_rostos = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, face_location in zip(codificacoes_rostos, face_locations):
        # Comparar a codificação do rosto com as codificações conhecidas
        matches = face_recognition.compare_faces(codificacoes_conhecidas, face_encoding)
        name = "Desconhecido"

        # Encontrar o índice do rosto correspondente e definir o nome
        if True in matches:
            first_match_index = matches.index(True)
            name = nomes_conhecidos[first_match_index]

        # Desenhar um retângulo e nome ao redor do rosto
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Mostrar o frame resultante
    cv2.imshow('Video', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video_capture.release()
cv2.destroyAllWindows()
