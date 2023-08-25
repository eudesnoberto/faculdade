import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Carregar o modelo InceptionV3
model = InceptionV3(weights='imagenet')

# Função para pesquisar e carregar a imagem
def browse_image():
    image_path = filedialog.askopenfilename()
    image_entry.delete(0, tk.END)
    image_entry.insert(0, image_path)

# Função para exibir as previsões e identificar a categoria
def display_predictions():
    image_path = image_entry.get()
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    result_label.config(text="Detalhes Pesquisados:")
    result_label.config(text=result_label.cget("text") + f"\n1: {decoded_predictions[0][1]} ({decoded_predictions[0][2]:.2f})")

    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

    # Identificar automaticamente a categoria
    category = decoded_predictions[0][1]
    if any(keyword in category.lower() for keyword in ["animal", "creature", "pet"]):
        category_label.config(text="Categoria: Animal")
    elif any(keyword in category.lower() for keyword in ["person", "human", "people"]):
        category_label.config(text="Categoria: Pessoa")
    else:
        category_label.config(text="Categoria: Objeto")

# Criar a janela
root = tk.Tk()
root.title("Detecção de Objetos")

# Botão para procurar a imagem
browse_button = tk.Button(root, text="Procurar Imagem", command=browse_image)
browse_button.pack()

# Rótulo e entrada para o caminho da imagem
image_label = tk.Label(root, text="Caminho da Imagem:")
image_label.pack()
image_entry = tk.Entry(root)
image_entry.pack()

# Botão para exibir as previsões e identificar a categoria
load_button = tk.Button(root, text="Exibir Detalhes", command=display_predictions)
load_button.pack(pady=10)

# Rótulo para a imagem
img_label = tk.Label(root)
img_label.pack()

# Rótulo para os detalhes pesquisados
result_label = tk.Label(root, text="Detalhes Pesquisados:")
result_label.pack()

# Rótulo para a categoria identificada
category_label = tk.Label(root, text="Categoria:")
category_label.pack()

root.mainloop()
