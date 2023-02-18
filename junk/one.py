# from two import a
# c=5
# print(a)
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import io
import base64

# # Open Image
# img = Image.open("C:\\Users\Tittu\Desktop\work\ihrd\exif_data_problem\ihrd_screening\pyfiles\DSCN0029.jpg",mode='r')
# img_byte_arr = img.tobytes()
# #print(img_byte_arr)

# b=base64.b64encode(img_byte_arr)
# #print(b)
# imgs=Image.open(io.BytesIO(b))
# imgs.show()

byteImgIO = io.BytesIO()
byteImg = Image.open(
    "C:\\Users\Tittu\Desktop\work\ihrd\exif_data_problem\ihrd_screening\pyfiles\DSCN0029.jpg")
byteImg.save(byteImgIO, "PNG")
byteImgIO.seek(0)
byteImg = byteImgIO.read()


# Non test code
dataBytesIO = io.BytesIO(byteImg)
imgs=Image.open(dataBytesIO)
imgs.show()



