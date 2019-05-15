# -*- coding: utf-8 -*-

import os
import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img
import argparse


#help message
parser = argparse.ArgumentParser(usage='Extending images by using keras. Extending configuration depends on generator in last part of this code.',add_help=True)
# 引数の追加
parser.add_argument('-t', '--target',default="target",help="The folder containing original images.")
parser.add_argument('-r', '--results',default="results",help="The folder containing augumented images.")
parser.add_argument('-n', '--newpart',default="aug_",help="The results will be like newpart_hoge.jpg, newpart_hoge2.jpg etc.")
parser.add_argument('-m', '--howmany',default=1,help="How many images do u wanna get from one image?")



args = parser.parse_args()


new_part = args.newpart

def draw_images(generator, x, dir_name, index,file):
    # 出力ファイルの設定
    save_name = new_part+file
    g = generator.flow(x, batch_size=1, save_to_dir=dir_name,save_prefix=save_name,save_format='jpg')


    # 1つの入力画像から何枚拡張するかを指定
    # g.next()の回数分拡張される
    for i in range(int(args.howmany)):
        bach = g.next()


if __name__ == '__main__':

    # 出力先ディレクトリの設定
    output_dir = args.results
    if not(os.path.exists(output_dir)):
        os.mkdir(output_dir)

    # 拡張する画像群の読み込み
    images = glob.glob(args.target+"/*")

    # 拡張する際の設定
    generator = ImageDataGenerator(
                    rotation_range=0, # 90°まで回転
                    width_shift_range=0, # 水平方向にランダムでシフト
                    height_shift_range=0, # 垂直方向にランダムでシフト
                    channel_shift_range=55.0, # 色調をランダム変更
                    shear_range=0, # 斜め方向(pi/8まで)に引っ張る
                    horizontal_flip=False, # 垂直方向にランダムで反転
                    vertical_flip=False # 水平方向にランダムで反転
                    )

    # 読み込んだ画像を順に拡張
    for i in range(len(images)):
        img = load_img(images[i])
        # 画像を配列化して転置a
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        # 画像の拡張
        draw_images(generator, x, output_dir, i,file=os.path.basename(images[i]))
