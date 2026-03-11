from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

# 初始化图片验证码生成器（字体路径根据实际情况调整）
image = ImageCaptcha(
    fonts=[
        "./fonts/ChelseaMarketsr.ttf",
        "./fonts/DejaVuSanssr.ttf",
    ]
)

# 生成初始6位数字验证码
random = str(randint(100000, 999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random, "out.png")


def verify():
    global random
    # 1. 去除输入内容的换行、空格（解决\n导致的ValueError）
    x = t1.get("0.0", END).strip()
    try:
        # 2. 先校验是否为空，再转int对比
        if not x:
            messagebox.showinfo("Error", "请输入验证码！")
            return
        if int(x) == int(random):
            messagebox.showinfo("success", "verified")
        else:
            messagebox.showinfo("Alert", "Not verified")
            refresh()
    except ValueError:
        # 3. 捕获非数字输入的异常
        messagebox.showinfo("Error", "请输入有效的数字验证码！")


def refresh():
    global random
    # 重新生成验证码
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, "out.png")
    # 加载新图片并更新标签（保留图片引用，防止tkinter回收）
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.photo = photo  # 关键修复：避免图片刷新后消失
    l1.update()
    # 4. 删除无效的UpdateLabel()调用（解决NameError）


# 构建GUI
root = Tk()
photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="submit", command=verify)
b2 = Button(root, text="refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()

root.mainloop()