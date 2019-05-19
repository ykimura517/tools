from PIL import Image
import numpy as np
import os

lines = 0
with open("./position.txt", "r") as f:
    lines = f.readlines()

data = []
for line in lines:
    line = line.replace("\n", "")
    a = line.split(",")
    data.append(a)

for d in data:
    d_name = d.pop(0)
    print(d_name)
    print(d)
    #sample_image = np.array(Image.open('D_shot03.jpg'))
    for i,position in enumerate(d):
        sample_name = d_name
        print(sample_name)
        sample_image = np.array(Image.open("sample/" + sample_name))
        position = position.split("_")
        print(position)
        height = sample_image.shape[0]
        width = sample_image.shape[1]
        p_wid = int(position[0])
        p_hei = int(position[1])
        if p_wid + 150 > width:
            right = width
            left = width -300
        elif p_wid - 150 < 0:
            right = 300
            left = 0
        else:
            right = p_wid + 150
            left = p_wid - 150

        if p_hei + 150 > height:
            up = height
            down = height - 300
        elif p_hei - 150 < 0:
            up = 300
            down = 0
        else:
            up = p_hei + 150
            down = p_hei - 150
        print(down,up,left,right)
        prop_sample = sample_image[down:up,left:right,:].astype('u1')
        prop_sample = Image.fromarray(prop_sample)

        '''if not os.path.isdir('detect_section'):
            os.makedirs('detect_section')'''

        if not os.path.isdir('nodetect_section'):
            os.makedirs('nodetect_section')

        #prop_im.save('detect_section/' + str(i) + '_' + d_name)
        prop_sample.save('nodetect_section/h_' + str(down) + '_' + str(up) + '_w_' + str(left) + '_' + str(right) + '_' +  d_name)
        
