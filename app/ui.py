import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 创建一个空白背景，大小为 600x400
image = np.ones((400, 600, 3), dtype=np.uint8) * 255

# 使用PIL在OpenCV图像上绘制中文
# 将numpy数组转换为PIL图像对象
pil_image = Image.fromarray(image)

# 创建画笔对象
draw = ImageDraw.Draw(pil_image)

# 选择一个支持中文的字体（可以根据实际字体路径修改）
font = ImageFont.truetype("msyh.ttc", 30)  # 微软雅黑字体

# 绘制车牌背景矩形
draw.rectangle([100, 150, 500, 250], fill="yellow")  # 黄色矩形模拟车牌

# 绘制车牌号（中文支持）
draw.text((180, 180), "粤A12345", font=font, fill="black")

# 添加系统名称
draw.text((70, 50), "车牌识别系统", font=font, fill="black")

# 添加提示信息
draw.text((150, 300), "点击左方按钮开始车牌识别", font=font, fill="red")

# 将PIL图像转换回OpenCV图像
image = np.array(pil_image)

# 保存图像
cv2.imwrite('pic/logo.png', image)

# 显示生成的图像
cv2.imshow('Home Page Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
