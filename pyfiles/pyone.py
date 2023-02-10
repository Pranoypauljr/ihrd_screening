from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

# Open Image
img = Image.open("C:\\Users\Tittu\Desktop\work\ihrd\pyfiles\DSCN0029.jpg")

#Get EXIF Data
exif_table = {}
for k, v in img._getexif().items():
    tag = TAGS.get(k)
    exif_table[tag] = v
#print(exif_table['GPSInfo'])
gps_info={}
for k, v in exif_table['GPSInfo'].items():
    geo_tag=GPSTAGS.get(k)
    gps_info[geo_tag]=v
#print(gps_info)
#Get Latitude and Longitude
lat = gps_info['GPSLatitude']
long = gps_info['GPSLongitude']
#Convert to degrees
lat = float(lat[0]+(lat[1]/60)+(lat[2]/(3600*100)))
long = float(long[0]+(long[1]/60)+(long[2]/(3600*100)))
#Negative if LatitudeRef:S or LongitudeRef:W
if gps_info['GPSLatitudeRef'] == 'S':
    lat = -lat
if gps_info['GPSLongitudeRef'] == 'W':
    long = -long
print(lat)
print("------")
print(long)
