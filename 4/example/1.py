# import PIL
from PIL import Image, ImageDraw,ImageFont
import random

# 1 生成画布
# 第一个参数：颜色模式：RGB、RGBA
# 第二个参数：画布的宽高 (宽,高)
# 点歌参数： 背景颜色：  单词     #rrggbb  (100,29,90)
# im = Image.new('RGB',(1000,500),'yellow')
im = Image.new('RGB',(1000,500),'white')

# 2生成画笔
pen = ImageDraw.Draw(im)


def rand_color():
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)


# 3 画点
for i in range(500):
    x = random.randint(1,1000)
    y = random.randint(1,500)
    pen.point((x,y),rand_color())
    # print(rand_color())

# 4 画线
pen.line([(0,0),(999,499)],'red',10)

# 5 rectangle
pen.rectangle([(100,50),(400,300)],fill='red',outline='gold',width=10)

# 画字
myFont = ImageFont.truetype('SIMLI.TTF',size=60,encoding='utf-8')
# print(myFont)

pen.text((330,20),'风景这边独好',fill=rand_color(),font=myFont)

# 6 保存图片
im.save('im.png')