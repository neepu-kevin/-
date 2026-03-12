from PIL import ImageFilter

from PIL import Image

import os
print(os.getcwd())

# 读取图像获得Image对象
image = Image.open('1.jpg')

image=image.filter(ImageFilter.CONTOUR)

image.save(r'new_image.jpg')