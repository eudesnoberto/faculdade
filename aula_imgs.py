from PIL import Image, ImageFilter

# Abrir a imagem
input_image = Image.open('imgs\linda.jpg')

# Aplicar um filtro de desfoque
blurred_image = input_image.filter(ImageFilter.GaussianBlur(10))

# Salvar a imagem resultante
blurred_image.save('imgs/imagem_desfocada.jpg')

print("Imagem desfocada salva.")
