import os
import glob
import argparse
import shutil


#help message
parser = argparse.ArgumentParser(usage='Make "target" folder and put images to be renamed in it. The renamed images will be in "results" folder.',add_help=True)
# 引数の追加
parser.add_argument('-c', '--copy',default=1,help="1:copy,0:move")
args = parser.parse_args()


#名前を変えたい画像たちをいれておくフォルダ名
target_folder = 'target'

path = target_folder+'/*'

files=glob.glob(path)

assert len(files)>0,"target folder is empty."


i=1

#コピーする場合
if bool(int(args.copy)):
    for img in files:
        shutil.copy(img, "results/"+str(i)+'.jpg')
        i+=1
#移動する場合
else:
    for img in files:
        os.rename(img,"results/"+str(i)+'.jpg')
        i+=1

#結果はresultsフォルダーに入る












#結果はresultsフォルダーに入る
