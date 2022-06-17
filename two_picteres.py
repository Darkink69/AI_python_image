import PIL.ImageGrab
from PIL import Image, ImageFilter, ImageDraw
import os

# Определяем рабочую директорию
dir = os.path.dirname(__file__)
dirInPath = os.path.join(dir)
onlyfiles = next(os.walk(dirInPath+'/in'))[2]
print(onlyfiles)
print(dirInPath)

# # Создаем новый холст с нужным размером
# img = Image.new('RGB', (600, 800))
# Открываем одну и вторую картинки
img1 = Image.open('nu2.png')
img2 = Image.open('Screenshot_3.png')

# Склеиваем 2 картинки с маской
mask = Image.open('horse.png').convert('L').resize(img1.size)
# mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
img = Image.composite(img1, img2, mask)

img.show()
img.save("out.jpg")


# Вставляем в нужные координаты первую, потом в нужные координаты вторую картинки
# img.paste(img1, (0, 0))
# img.paste(img2, (100, 50))

# # ресайз
# y = dirInPath + '/in/' + onlyfiles[2]
# print(y)
# x = Image.open(y)
# x = Image.open('C:/Users/varkatov/imageAI/face/image2.jpg')
# x = x.resize((160, 90), Image.ANTIALIAS)
# x.show()
# x.save(onlyfiles[2])
# #
# # Делаем скриншот
# # screenShot = PIL.ImageGrab.grab()
# # screenShot.show()
#
# img.show()
# img.save("out.jpg")





# try:
#     # загружаем изображение с жесткого диска
#     original = Image.open("toony_out1.jpg")
# except FileNotFoundError:
#     print("Файл не найден")

# print("Размер изображения:")
# print(original.format, original.size, original.mode)
# # размываем изображение
# blurred = original.filter(ImageFilter.BLUR)
# cropped = original.crop((0, 80, 200, 400))
# # открываем оригинал и размытое изображение
# # blurred.show()
# # сохраняем изображение
# blurred.save("blurred.png")
# cropped.save("crop.png")
