import ffmpeg
import os

cmd = 'ffmpeg -i 1.mp4 -vf "noise=alls=20:allf=t+u" 22.mp4'
# cmd = 'ffmpeg -i 1.mp4 -r 1 -f image2 image-%2d.png'
os.system(cmd)

# stream = ffmpeg.input('1.mp4')
# stream2 = ffmpeg.input('IMG.png')
# print(ffmpeg.probe(stream)['streams'][0]['duration'])
# stream = ffmpeg.overlay(stream, stream2, {100: 200})
# stream = ffmpeg.filter([stream, stream2], 'overlay', 100, 100)

# Оттенок насыщенность
# stream = ffmpeg.hue(stream, h=90, s=5, b=3)

# stream = ffmpeg.

# rgb + r + g + b + alpha от -2 до 2
# stream = ffmpeg.colorchannelmixer(stream, gg=2, ga=-2)

# stream = ffmpeg.crop(stream, 20, 50, 100, 200)
# stream = ffmpeg.output(stream, 'output.mp4').run()


# Изменение fps
# (
#     ffmpeg
#     .input('1.mp4')
#     .filter('fps', fps=120, round='up')
#     .output('dummy2.mp4')
#     .run()
# )

# Разбираем на картинки
# (
#     ffmpeg
#         .input('1.mp4')
#         .output('PIC-%d.png')
#         .run()
# )

# Собираем из картинок видео
# (
#     ffmpeg
#         .input('PIC-%d.png')
#         .output('222.mp4')
#         .run()
# )