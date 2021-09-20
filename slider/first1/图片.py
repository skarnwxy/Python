from os import listdir
from PIL import Image



def pinjie():
    # 获取当前文件夹中所有JPG图像
    im_list = [Image.open('F:/picture/') for fn in listdir() if fn.endswith('.png')]
    img1 = Image.open('F:/picture/29.png')
    img2 = Image.open('F:/picture/33.png')
    im_list.append(img1)
    im_list.append(img2)
    # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = i.resize((1280, 1280), Image.BILINEAR)
    ims.append(new_img)

    # 单幅图像尺寸
    width, height = ims[0].size

    # 创建空白长图
    result = Image.new(ims[0].mode, (width, height * len(ims)))

    # 拼接图片
    for i, im in enumerate(ims):
        result.paste(im, box=(0, i * height))

    # 保存图片
    result.save('F:/picture/res1.jpg')


if __name__ == '__main__':
    pinjie()