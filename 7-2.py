from PIL import Image
image = 'прога.png'
with Image.open('прога.png') as img:
    img.load()
image2 = img.resize((img.width // 3, img.height // 3 ))
image2.save('прога1.png')
image3 = img.transpose(Image.FLIP_TOP_BOTTOM)
image3.save('прога2.png')
image3 = img.transpose(Image.FLIP_LEFT_RIGHT)
image3.save('прога3.png')


