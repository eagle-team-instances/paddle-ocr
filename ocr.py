# import paddle
# print(paddle.__version__)
from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './img/img_1.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

# 显示结果
from PIL import Image
from PIL import ImageFont
font = ImageFont.load_default()

image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='Roboto-Light.ttf')
# im_show = draw_ocr(image, boxes, txts, scores, font_path=font)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')