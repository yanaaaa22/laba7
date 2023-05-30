from PIL import Image
new_image = Image.new('RGBA', (770, 768))
main_img = Image.open('3.jpg').convert("RGBA")
watermark_img = Image.open('2.png')
new_image.paste(watermark_img, (0, 0))
new_image = Image.alpha_composite(main_img, new_image)
new_image.save('watermark.png')


