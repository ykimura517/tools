import shutil
import glob
import os

how_many_img=50
imgs=glob.glob("./*.jpg")

for img in imgs:
    for i in range(how_many_img):
        shutil.copy(img,os.path.basename(img).replace(".jpg","")+str(i)+".jpg")
