from PIL import Image
from tqdm import tqdm
import scipy.io as scio
import os

# 路径准备
dataset_name = 'HandDetectionDataset'
mat_base_path = 'hand_dataset/training_dataset/training_data/'
mat_label_path = mat_base_path+'annotations/'
mat_img_path = mat_base_path+'images/'

xml_base_path = 'HandDetectionDataset/'
xml_label_path = xml_base_path+'Annotations/'
xml_img_path = xml_base_path+'JPEGImages/'

# mat文件中标识框的名字，此处为boxes
key_name = 'boxes'

# 读取标注路径下的所有.mat格式标注的文件名
mat_annotations = os.listdir(mat_label_path)

for mat in tqdm(mat_annotations):
    # 过滤掉'.'开头的隐藏文件
    if mat[0] == '.':
        continue
    # 读取图片信息
    img_name = mat.split(".")[-2]+'.jpg'
    img_path = mat_img_path+img_name
    img = Image.open(img_path)
    imgWidth, imgHeight = img.size

    #打开xml文件
    xml_file = open(xml_label_path+mat.split(".")[-2]+'.xml', 'w')

    xml_file.write('<annotation>\n')
    xml_file.write('\t<folder>' + dataset_name + '</folder>\n')
    xml_file.write('\t<filename>' + img_name + '</filename>\n')
    xml_file.write('\t<size>\n')
    xml_file.write('\t\t<width>' + str(imgWidth) + '</width>\n')
    xml_file.write('\t\t<height>' + str(imgHeight) + '</height>\n')
    xml_file.write('\t\t<depth>' + str(3) + '</depth>\n')
    xml_file.write('\t</size>\n')
    xml_file.write('\t<segmented>0</segmented>\n')

    load_data = scio.loadmat(mat_label_path+mat)

    #为图像中每个手部标注进行记录
    for i in range(len(load_data[key_name][0])):
        xml_file.write('\t<object>\n')
        xml_file.write('\t\t<name>hand</name>\n')
        xml_file.write('\t\t<pose>Unspecified</pose>\n')
        xml_file.write('\t\t<truncated>0</truncated>\n')
        xml_file.write('\t\t<difficult>0</difficult>\n')
        xml_file.write('\t\t<bndbox>\n')
        xmin=load_data[key_name][0][i][0][0][0][0][0]
        ymin=load_data[key_name][0][i][0][0][0][0][1]
        xmax=xmin
        ymax=ymin
        #确定xmin，ymin，xmax，ymax 
        for j in range(3):
            if load_data[key_name][0][i][0][0][j+1][0][0]<xmin:
                xmin=load_data[key_name][0][0][0][0][j+1][0][0]
            if load_data[key_name][0][i][0][0][j+1][0][1]<ymin:
                ymin=load_data[key_name][0][0][0][0][j+1][0][1]
            if load_data[key_name][0][i][0][0][j+1][0][0]>xmax:
                xmax=load_data[key_name][0][0][0][0][j+1][0][0]
            if load_data[key_name][0][i][0][0][j+1][0][1]>ymax:
                ymax=load_data[key_name][0][0][0][0][j+1][0][1]
        xml_file.write('\t\t\t<xmin>'+str(xmin)+'</xmin>\n')
        xml_file.write('\t\t\t<ymin>'+str(ymin)+'</ymin>\n')
        xml_file.write('\t\t\t<xmax>'+str(xmax)+'</xmax>\n')
        xml_file.write('\t\t\t<ymax>'+str(ymax)+'</ymax>\n')
        xml_file.write('\t\t</bndbox>\n')
        xml_file.write('\t</object>\n')
    xml_file.write('</annotation>\n')
    xml_file.close()
