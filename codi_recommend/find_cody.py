import re

def isHangul(text):
    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    return hanCount > 0


import pandas as pd
import numpy as np

temp = pd.read_csv('csv/stylist_table.csv')
temp.drop('Unnamed: 0',axis=1,inplace=True)

temp_save = temp.copy()

category_table = pd.read_csv('csv/category_table.csv')
color_table = pd.read_csv('csv/color_table.csv')
color_table.drop('Unnamed: 0',axis=1,inplace=True)
lang = ['eng','kor']

# 데이터 색상 매칭 & 매칭 안되면 삭제(플라워color 이런거 거름)
for m in temp:
    chk ={0:False,1:False,2:False}
    for color_cnt in range(len(color_table)):
        for i in lang:
            for j in range(3):
                if color_table[i][color_cnt].lstrip() in str(temp[m][j * 2]).lower():
                    temp_save[m][j*2] = color_table['eng'][color_cnt].lstrip()
                    chk[j]=True

    for i,j in enumerate(chk.values()):
        if j==False:
            temp_save[m][i*2] = np.nan
            temp_save[m][i*2+1] = np.nan

#1개만 남은 데이터 컬럼 삭제
for i in temp_save:
    if(temp_save[i].notnull().sum())<3:
        temp_save.drop(i, axis=1, inplace=True)

#카테고리 분류 작업
for i in temp_save:
    cnt=0
    chk = False
    for j in temp_save[i]:
        for k in category_table:
            for l in category_table[k]:
                if l == j:
                    temp_save[i][cnt] = k
        cnt+=1


#한글 제거 부분
for i in temp_save:
    cnt=0
    for j in temp_save[i]:
        try:
            if(ord('가') <= ord(j[0]) <= ord('힣')):
                temp_save[i][cnt] = np.nan
                temp_save[i][cnt-1] = np.nan
        except TypeError:
            pass
        cnt+=1

# 2개 이하 데이터 제거(코디 추천 불가 하기 때문)
for i in temp_save:
    if(temp_save[i].notnull().sum())<3:
        temp_save.drop(i, axis=1, inplace=True)


temp_save.to_csv('csv/stylist_table_clean.csv',encoding='utf-8-sig')

