from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import io
import base64
img = Image.open("C:\\Users\Tittu\Desktop\work\ihrd\exif_data_problem\ihrd_screening\pyfiles\DSCN0029.jpg",mode='r')
img_byte_arr = img.tobytes()
#print(img_byte_arr)

b=base64.b64encode(img_byte_arr)
print(b)
