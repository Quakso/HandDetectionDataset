
from PIL import Image
import scipy.io as scio
import os

#路径准备
dataset_name='HandDetectionDataset'
mat_base_path='hand_dataset/training_dataset/training_data/'
mat_label_path=mat_base_path+'annotations/'
mat_img_path=mat_base_path+'images'

xml_base_path='HandDetectionDataset/'
xml_label_path=xml_base_path+'Annotations/'
xml_img_path=xml_base_path+'JPEGImages'

#mat文件中标识框的名字，此处为boxes
key_name='boxes'

#读取标注路径下的所有.mat格式标注的文件名
mat_annotations=os.listdir(mat_label_path)

load_data=scio.loadmat(mat_label_path+'Buffy_1.mat')
print(load_data)
print(load_data[key_name][0][0])
print(load_data[key_name][0][1])

xmin=load_data[key_name][0][0][0][0][0][0][0]
ymin=load_data[key_name][0][0][0][0][0][0][1]
print(xmin)
print(ymin)
xmax=xmin
ymax=ymin

for i in range(3):
    if load_data[key_name][0][0][0][0][i+1][0][0]<xmin:
        xmin=load_data[key_name][0][0][0][0][i+1][0][0]
    if load_data[key_name][0][0][0][0][i+1][0][1]<ymin:
        ymin=load_data[key_name][0][0][0][0][i+1][0][1]
    if load_data[key_name][0][0][0][0][i+1][0][0]>xmax:
        xmax=load_data[key_name][0][0][0][0][i+1][0][0]
    if load_data[key_name][0][0][0][0][i+1][0][1]>ymax:
        ymax=load_data[key_name][0][0][0][0][i+1][0][1]
print(xmin)
print(ymin)
print(xmax)
print(ymax)
        



