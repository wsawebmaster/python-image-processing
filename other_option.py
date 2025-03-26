from PIL import Image # Usando Pillow

# mostrar
imagem = Image.open("imagens/image.png")

imagem.show()

# converter (save as jpg)
# tentar direto, se der erro, tornar RGB e converter em jpg
imagem_rgb = imagem.convert("RGB")
imagem_rgb.save("imagens/image.jpg")

# resize (muito util em servidores/sites) - sempre partindo da maior para a menor, se n você zoa o rolê
tamanho = (500, 500)
imagem.thumbnail(tamanho)
imagem.save("imagens/image500px.png")

tamanho = (300, 300)
imagem.thumbnail(tamanho)
imagem.save("imagens/image300px.png")

# editar a imagem

# rotate
imagem.rotate(180).save("imagens/image_baixo.png")

# preto e branco
imagem.convert("L").save("imagens/image_preto_branco.png")

# filtros
from PIL import ImageFilter

imagem.filter(ImageFilter.GaussianBlur(20)).save("imagens/image_blur.png")