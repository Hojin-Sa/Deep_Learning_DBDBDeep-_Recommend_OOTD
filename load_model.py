import tensorflow as tf
import cv2
import numpy as np
import os
import pandas as pd
import numpy as np
import natsort


## params
img_size = 224
img_shape = (img_size,img_size,3)
batch_size = 32
epochs = 5
dropout_rate = 0.5
num_of_predict = 4
labels = ['Not sure', 'T-Shirt', 'Shoes', 'Shorts', 'Shirt', 'Pants',
 'Skirt', 'Other', 'Top', 'Outwear', 'Dress', 'Body', 'Longsleeve', 'Undershirt',
 'Hat', 'Polo', 'Blouse', 'Hoodie', 'Skip', 'Blazer']
big_labels = {'상의':['T-Shirt','Shirt','Top','Outwear','Longsleeve','Polo','Outwear','Blouse','Hoodie','Blazer'],
              '하의':['Shorts','Pants','Skirt',],
              '신발':['Shoes'],
              '그 외':['Not sure','Other','Dress', 'Body','Hat','Undershirt']}

def predict_output(model, in_path):
    img = cv2.imread(in_path)
    img = cv2.resize(img, (img_size, img_size))  # resize image to match model's expected sizing
    img = np.reshape(img, [1, img_size, img_size, 3])
    img = img / 255.
    out = model.predict(img)
    return (np.argmax(out))
def load_model():
    model = tf.keras.models.load_model('eff_final.h5')
    return model


import math
from collections import Counter


def find_nearest(array, value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx - 1]) < math.fabs(value - array[idx])):
        return array[idx - 1]
    else:
        return array[idx]


def get_color_distance(a, b):
    tmp = 0
    for x in range(3):
        tmp += (a[x] - b[x]) ** 2
    return math.sqrt(tmp)


def split_map(x):
    return list(map(int, x.split(',')))


color_table = pd.read_csv('color_table (2).csv')
table_list = list(color_table['rgb'].values)
table_list = list(map(split_map, table_list))
table_col = list(color_table['eng'].values)


def return_color(path):

    img = cv2.imread(path)
    img = cv2.resize(img, (img_size, img_size))
    color = []
    color.append(img[int(img.shape[0] / 2)][int(img.shape[1] / 2)].tolist()[::-1])
    color.append(img[int(img.shape[0] / 4)][int(img.shape[1] / 4)].tolist()[::-1])
    color.append(img[int(img.shape[0] * 3 / 4)][int(img.shape[1] / 4)].tolist()[::-1])
    color.append(img[int(img.shape[0] / 4)][int(img.shape[1] * 3 / 4)].tolist()[::-1])
    color.append(img[int(img.shape[0] * 3 / 4)][int(img.shape[1] * 3 / 4)].tolist()[::-1])

    color_dis = []
    all_color = []
    for col in color:
        color_dis = []
        for x in table_list:
            color_dis.append(get_color_distance(col, x))
        all_color.append(table_col[np.argmin(color_dis)])
    cnt = Counter(all_color)
    return list(cnt)[0]

def return_data_frame(model,dir_path):
    path = list(os.listdir(dir_path))
    path = [file for file in path if file.endswith((".jpeg",",png",".jpg"))]
    path = natsort.natsorted(path)
    print(path)
    big_labels = {'상의':['T-Shirt','Shirt','Top','Outwear','Longsleeve','Polo','Outwear','Blouse','Hoodie','Blazer'],
              '하의':['Shorts','Pants','Skirt',],
              '신발':['Shoes'],
              '그 외':['Not sure','Other','Dress', 'Body','Hat','Undershirt']}
    outs = []

    #model = load_model()
    dht_list = []
    tor_list = []
    for x in path:
        inputs = dir_path + x
        dht_list.append(labels[predict_output(model, inputs)])
        tor_list.append(return_color(inputs))
    for x in dht_list:
        if x in big_labels['상의']:
            outs.append('상의')
        elif x in big_labels['하의']:
            outs.append('하의')
        elif x in big_labels['신발']:
            outs.append('신발')
        else:
            outs.append('그 외')
    out_dataframe = pd.DataFrame({'대분류':outs,'중분류':dht_list,'색':tor_list})
    return out_dataframe