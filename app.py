from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import io
import base64
import json

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class img(db.Model):
    img_id=db.Column(db.Integer,primary_key=True)
    # act_name=db.Column(db.String(200),primary_key=True)
    # content=db.Column(db.String(200),nullable=False)
    # completed=db.Column(db.Integer,default=0)
    # date_created=db.Column(db.DateTime,default=datetime.utcnow)

    images=db.Column(db.BLOB,nullable=False)
    latitude=db.Column(db.FLOAT,nullable=False)
    longitude=db.Column(db.FLOAT,nullable=False)
    link=db.Column(db.String(2000),nullable=False)
    
    def __repr__(self):
        return '<images %r>' % self.images

count = 2

@app.route('/',methods=['POST','GET'])
def index():
    global count
    if(request.method=='POST'):
        f=request.files['image']
        print(f)
        f.save(f.filename) 
        f = open(f.filename, 'rb')
        file_content = f.read()
        str_b=file_content
        lat,long=exif_data(file_content)
        src = "https://wiki-map.com/map/?locale=en&lat="+str(lat)+"&lng="+str(long)
        new_image=img(img_id=count,images=str_b,latitude=lat,longitude=long,link=src)
        count+=1
        db.session.add(new_image)
        db.session.commit()
        return redirect('/') 
        
        #return('Error happended during post req')

    else:
        images=img.query.all()
        for image in images:
              #print(type(image.images))
            
              strs = str(base64.b64encode(image.images))
              
              
              #print(type(strs))  
            # strs=strs.decode("UTF-8")
              image.images="data:image/jpg;base64,"+(strs[2:-1])
        return render_template('index.html',images=images)

def exif_data(exif_data):
    dataBytesIO = io.BytesIO(exif_data)
    img=Image.open(dataBytesIO)
    # Get EXIF Data
    exif_table = {}
    for k, v in img._getexif().items():
        tag = TAGS.get(k)
        exif_table[tag] = v
    # print(exif_table['GPSInfo'])
    gps_info = {}
    for k, v in exif_table['GPSInfo'].items():
        geo_tag = GPSTAGS.get(k)
        gps_info[geo_tag] = v
    # print(gps_info)
    # Get Latitude and Longitude
    lat = gps_info['GPSLatitude']
    long = gps_info['GPSLongitude']
    # Convert to degrees
    lat = float(lat[0]+(lat[1]/60)+(lat[2]/(3600*100)))
    long = float(long[0]+(long[1]/60)+(long[2]/(3600*100)))
    # Negative if LatitudeRef:S or LongitudeRef:W
    if gps_info['GPSLatitudeRef'] == 'S':
        lat = -lat
    if gps_info['GPSLongitudeRef'] == 'W':
        long = -long
    return(lat,long)
    # print("------")
    # print(long)
# def bytearr(exif_data):
#     # img = Image.open(
#     #     exif_data, mode='rb')
#     img_byte_arr = exif_data.tobytes()
#     # print(img_byte_arr)
#     b = base64.b64encode(img_byte_arr)
#     return(b)


if __name__== "__main__":
    app.run(debug=True)