from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

'''
	随机生成验证码
'''


# 随机字母
def ranchr():
    return chr(random.randint(65, 90))


# 随机颜色1
def rancolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rancolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 设置图片
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rancolor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), ranchr(), font=font, fill=rancolor2())
# 模糊处理
image = image.filter(ImageFilter.BLUR)
# 保存
image.save('code.jpg', 'jpeg')




