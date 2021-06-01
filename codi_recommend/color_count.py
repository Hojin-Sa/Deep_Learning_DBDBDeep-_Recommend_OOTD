import pandas as pd
import numpy as np
temp_color_table = pd.read_csv('csv/color_table.csv')
temp_stylist = pd.read_csv('csv/stylist_table_clean.csv')

temp_dict = {}
category = temp_color_table['eng'].unique()
new_category = []

for i in category:
    new_category.append(i.lstrip())

for i in new_category:
    temp_dict[i] = 0
temp_key = list(temp_dict.keys())

for i in temp_stylist:
    for j in range(3):
        if ((temp_stylist[i][j*2]) in temp_key):
            temp_dict[temp_stylist[i][j*2]] += 1

temp_dict = sorted(temp_dict.items(),key=lambda x:x[1],reverse=True)

print(temp_dict)