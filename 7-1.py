from PIL import Image
image = Image.open('прога.png')
with Image.open('прога.png') as img:
    img.load()
    image.show()

width = img.width
height = img.height
print("Высота изображения: ", height)
print("Ширина изображения: ", width)
print("Формат изображения: ", img.format)
print("Цветовая модель изображения: ", img.mode)

