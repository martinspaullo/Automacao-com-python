from PIL import Image, ImageEnhance, ImageFilter #Vamos usar o pilow
# outra opção,   "pip install scikit-image"  https://scikit-image.org/docs/0.25.x/user_guide/install.html

# 1 - Importando a Imagem / Convertendo a imagem em escala de cinza
img = Image.open('data/DK2.webp')
# print(img)
img.show()

gray_img = img.convert('L')
# gray_img.show()

# 2 - ****** Utilizando Operações em Imagem I ******

#Rotacionando imagens
rotated_img = img.rotate(180)
# rotated_img.show()

#Transposiçao da imagens, Angulo de visualização da imagens
transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
#transpose_img.show()

# diminuiu o tamanho da img
resize_img_small = img.resize((300, 200))
# resize_img_small.show()

#Aumenta o tamanho da imagem
resize_img_big = img.resize((1500, 1000))
#resize_img_big.show()

#Corte da  imagem
dim = (200, 200, 250, 300)
crop_img = img.crop(dim)
#crop_img.show()


# 3 - ****** Utilizando Operações em Imagem II ********

# brilho da img
enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(3)

#bright_img.show()

#contraste da img
enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(3)
#contrast_img.show()

# 4 - Utilizando Filtros
filtro_blur = img.filter(ImageFilter.CONTOUR)
filtro_blur.show()
