import cv2

# Carregar o modelo de detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar o modelo de reconhecimento de rosto
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read('modelo.yml')

# Inicializar a webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capturar um frame
    ret, frame = video_capture.read()

    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Reconhecer o rosto
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_roi)
        if confidence < 100:
            name = "Pessoa"
        else:
            name = "Desconhecido"

        # Desenhar retângulos ao redor dos rostos detectados
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (x + 6, y - 6), font, 0.5, (255, 255, 255), 1)

    # Mostrar o frame resultante
    cv2.imshow('Video', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video_capture.release()
cv2.destroyAllWindows()
