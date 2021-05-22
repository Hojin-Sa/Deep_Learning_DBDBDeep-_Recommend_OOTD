from PIL import Image
# 반복문으로 사진 resize
# for i in range(1, 6):
#     st = 'img/dress/dress'
#     stjpeg = st+str(i)+'.jpeg'
#     image = Image.open(str(stjpeg))
#     image_resize = image.resize((200,200))
#     image_resize.save(st+'1'+str(i)+'.jpeg')

# 사진한개만 resize
image = Image.open('img/20.jpeg')
image_resize = image.resize((200,200))
image_resize.save('img/top/top11.jpeg')
