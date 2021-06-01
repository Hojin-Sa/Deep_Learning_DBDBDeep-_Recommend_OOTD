from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import pandas as pd


def hex_to_rgb(hex_color):
    hex_color = hex_color.replace(" ", "").replace("#", "")
    # 3-digits hex color
    if len(hex_color) == 3:
        r = hex_color[0] * 2
        g = hex_color[1] * 2
        b = hex_color[2] * 2
    # 6-digits hex color
    elif len(hex_color) == 6:
        r = hex_color[0:2]
        g = hex_color[2:4]
        b = hex_color[4:6]
    else:
        return "length error"
    # convert hex to decimal
    r = int(r, 16)
    g = int(g, 16)
    b = int(b, 16)
    # check if in range 0~255
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    # write rgb in correct syntax
    rgb_color = "{0},{1},{2}".format(r, g, b)
    return rgb_color


driver = webdriver.Chrome(
    executable_path= './chromedriver'
)

url = "https://supervitamin.tistory.com/76"
driver.get(url)
action = ActionChains(driver)
temp_kor = []
temp_eng = []
temp_rgb = []
temp_ycbcr = []


for i in range(3,143):
    temp_kor.append(driver.find_element_by_xpath('//*[@id="content"]/article/section[1]/div/center/table/tbody/tr['+str(i)+']/td[1]/font').text)
    temp_eng.append(driver.find_element_by_xpath('//*[@id="content"]/article/section[1]/div/center/table/tbody/tr['+str(i)+']/td[2]/font').text)
    temp_rgb.append(hex_to_rgb(driver.find_element_by_xpath('//*[@id="content"]/article/section[1]/div/center/table/tbody/tr['+str(i)+']/td[5]/div/font').text))

for i in temp_rgb:
    temp = i.split(",")
    y = str(round(0.299*float(temp[0]) + 0.587*float(temp[1]) + 0.114*float(temp[2]) ,2))
    cb = str(round((-0.16874*float(temp[0])) + (-0.33126*float(temp[1])) + 0.5*float(temp[2]) + 128 ,2))
    cr = str(round(0.5*float(temp[0]) + (-0.41869*float(temp[1])) + -0.08131*float(temp[2]) + 128 ,2))
    ycbcr = y+","+cb+","+cr
    temp_ycbcr.append(ycbcr)

df = pd.DataFrame([x for x in zip(temp_kor,temp_eng,temp_rgb,temp_ycbcr)],columns=['kor','eng','rgb','ycbcr'])

df.to_csv('color_table.csv',encoding='utf-8-sig')


