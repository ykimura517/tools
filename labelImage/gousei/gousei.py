import xml.etree.ElementTree as ET
import glob
import os
from PIL import Image
import numpy as np
import cv2
import random

#貼付け後の画像サイズ（touple）と貼り付けた場所の座標を返す size xmin,xmax ymin ymax
def ImgHarituke(baseImg,harituke_img,resultName):
    #最終的な貼り付けもと画像：数字がはいっていないもの
    base =cv2.imread(baseImg)
    print(base[0][0].shape)
    # size=(300,300,3)
    size=base.shape
    print(size)
    #harituke ind



    #f.jpgをblamk.jpgのx,yにはりつけるコード
    #つまり真っ黒画像に一旦貼り付ける

    f=Image.open(harituke_img)
    tt=np.zeros(size)
    cv2.imwrite("blank.jpg",tt)
    # tt.save("blank.jpg")
    tt = Image.open("blank.jpg")

    x=int(np.random.rand()*(size[1]-np.asarray(f).transpose(2,0,1).shape[2]-1)) #貼り付け場所　運に寄ってははりつけ画像が
    y=int(np.random.rand()*(size[0]-np.asarray(f).transpose(2,0,1).shape[1]-1))
    print(x,y)
    tt.paste(f,(x,y))
    tt.save("getwi.jpg")


    # baseにgetwiを透過貼り付け
    out = np.zeros(base.shape)
    harituke = cv2.imread("getwi.jpg")
    for i in range(base.shape[0]):
        for k in range(base.shape[1]):
            out[i][k]= base[i][k] if (harituke[i][k][0]<=20 and harituke[i][k][1]<=20) and harituke[i][k][2]<=20 else harituke[i][k]
    cv2.imwrite(resultName,out)

    xmin = x
    ymin = y
    xmax = xmin +np.asarray(f).transpose(2,0,1).shape[2]
    ymax = ymin +np.asarray(f).transpose(2,0,1).shape[1]
    return size,xmin,xmax,ymin,ymax


#xmin~ymaxをxmlに書き込む


#ImgSizeTouple(w,h,d)       BBTouple (xmin,xmax,ymin,ymax)
#eg. createXml(iwaki.xml,size,xmin,ymin,xmax,ymax)-----> <filename>iwaki3.jpg</filename> みたいな感じになる
def createXml(ImgSizeTouple,BBTouple,resultName,base_xml="base.xml",img_name="iwakirei.jpg",):


    # xml_files = glob.glob("xml/*.xml")
    tree = ET.parse(base_xml)
    root = tree.getroot()

    #change xml

    for filename in root.iter("filename"):
        filename.text = img_name



    for path in root.iter("path"):
        path.text = img_name

    for width in root.iter("width"):
        width.text = str(ImgSizeTouple[0])

    for height in root.iter("height"):
        height.text = str(ImgSizeTouple[1])

    for depth in root.iter("depth"):
        depth.text = str(ImgSizeTouple[2])

    for xmin in root.iter("xmin"):
        xmin.text = str(BBTouple[0])
    for xmax in root.iter("xmax"):
        xmax.text = str(BBTouple[1])
    for ymin in root.iter("ymin"):
        ymin.text = str(BBTouple[2])
    for ymax in root.iter("ymax"):
        ymax.text = str(BBTouple[3])

    for na in root.iter("name"):
        na.text = num_name




    #save
    tree.write(resultName)

if __name__ == "__main__":
    howManyDataDoyouWant = 1


    for i in range(10):
        num_name = str(i) #haritukeru suuji 1tumade


        rawimgs=glob.glob("raw-img/*.jpg")
        numbers=glob.glob("numbers/"+num_name+"/*.png")

        for i in range(howManyDataDoyouWant):

            baseImg = random.choice(rawimgs)
            harituke_img=random.choice(numbers) #数字のみの画像

            size,xmin,xmax,ymin,ymax=ImgHarituke(baseImg,harituke_img,"result-img/"+num_name+"-"+str(i)+".jpg")
            createXml((size[1],size[0],size[2]),(xmin,xmax,ymin,ymax),"result-xml/"+num_name+"-"+str(i)+".xml",img_name=num_name+"-"+str(i)+".jpg")
