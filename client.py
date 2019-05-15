import socket
import numpy as np
import sys
from time import localtime
import os
import time

target_host = "XXXX"
target_port = XXXX

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #ソケット作成
print(socket.AF_INET, socket.SOCK_STREAM)
print(client)
print(type(client))

client.connect((target_host, target_port))                      #サーバのIPとポートで接続
print ("Connect Success!! %s : %s" % (target_host, target_port))



def send_img(image_path):

    with open(image_path,"rb") as f:
        chunk = 5
        while True:
            fragment = f.read(chunk)
            client.sendall(fragment)
            print(fragment)
            print(len(fragment))
            if len(fragment) == 0:

                print("EOF")
                break


def recieve_img():

    now_time = str(localtime().tm_hour) + "-" + str(localtime().tm_min) + "-" + str(localtime().tm_sec)
    save_dir = "./client_img/"
    os.makedirs(save_dir, exist_ok = True)
    save_path = save_dir + now_time + ".jpg"
    #save_path = save_dir + now_time + ".png"
    f = open(save_path,"wb")

    while True:
        response = client.recv(10)
        time.sleep(0.000001)
        f.write(response)
        print(response)
        print(len(response))
        if len(response) < 10:
            print("EOF")
            f.close()
            break


def main():
    args = sys.argv[1]
    send_img(args)
    recieve_img()

if __name__ == "__main__":
    main()
