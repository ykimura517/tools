from PIL import Image
import glob
import argparse


#help message
parser = argparse.ArgumentParser(usage='Make "target" folder and put images to be renamed in it. The renamed images will be in "results" folder.',add_help=True)
# 引数の追加
parser.add_argument('-s', '--size',default=(300,300),help="This code cnverts images into (xx,yy) size. Please see the code")

args = parser.parse_args()


#名前を変えたい画像たちをいれておくフォルダ名
target_folder = 'target'
path = target_folder+'/*'

files=glob.glob(path)

assert len(files)>0,"target folder is empty."



#結果はresultsフォルダーに入る

images = glob.glob("target/*")
m=1

for image in images:

    img = Image.open(image)


    img_resize_lanczos = img.resize(args.size, Image.LANCZOS)
    img_resize_lanczos.save('results/'+str(m)+'.jpg')
    m+=1
