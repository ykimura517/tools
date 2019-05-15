import socket
import numpy as np
import os
import cv2
from contextlib import closing
from time import localtime
from PIL import Image
import time

#tcp config
host_ip =  'XXXX'        #ホストのIPを取る
port = XXXX

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ソケット作成
server.bind((host_ip, port))                             #IPとポート結び付け
server.listen(2)                                            #接続数
print ("[*]Server waiting on %s : %s" % (host_ip, port))
print("Loading SSD...")
from SSD import ssd
print("OK!")

save_dir = "./server_img/"
ssd_dir = "./server_img/ssd/"
os.makedirs(save_dir,exist_ok=True)
os.makedirs(ssd_dir, exist_ok=True)



def recieve_img(client,save_path):
    f = open(save_path,"wb")

    while True:
        response = client.recv(5)
        f.write(response)
        # print(response)
        # print(len(response))
        time.sleep(0.00001)
        if len(response) < 5:
            f.close()
            print("EOF")
            break


def send_img(client,ssd_path):                                         #送るメッセージ入力
    with open(ssd_path,"rb") as f:
        chunk = 10
        count = 0
        while True:
            #count = count+1

            fragment = f.read(chunk)
            client.sendall(fragment)
            print(fragment)
            print(count)

            if len(fragment) == 0:
                print("EOF")
                break


def main():
    while True:

        client, addr = server.accept()

        print ("[Connection from %s:%s ]" % (addr[0], addr[1]))
        now_time = str(localtime().tm_hour) + "-" + str(localtime().tm_min) + "-" + str(localtime().tm_sec)
        save_path = save_dir + now_time + ".jpg"
        ssd_path = ssd_dir + now_time + ".jpg"
        print(now_time)
        recieve_img(client,save_path)
        file_size = os.path.getsize(save_path)
        if file_size != 0 :
            ssd(save_path,ssd_path)
            send_img(client,ssd_path)
        else :
            print("画像が送られていません")

        client.close()

if __name__ == "__main__":
    main()
