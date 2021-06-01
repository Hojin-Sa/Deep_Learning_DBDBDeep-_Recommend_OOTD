from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import time
import pandas as pd
import numpy as np

driver = webdriver.Chrome(
    executable_path='./chromedriver'
)
stylist_data = pd.DataFrame()
count = 0
for sex in range(2):  # 남성, 여성 별 크롤링
    count+=1
    url = "https://store.musinsa.com/app/styles/lists?source=M_MUSINSA_NEWS/"
    driver.get(url)
    action = ActionChains(driver)
    if count%2==1:
        driver.find_element_by_xpath('//*[@id="default_top"]/div[2]/button[' + str(sex + 2) + ']').send_keys(Keys.ENTER)
    else:
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/div[4]/div/div[1]/div/div/a[13]').send_keys(Keys.ENTER)
    for page in range(10):  # 페이지별 크롤링
        print('page : ',page)
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/div[4]/div/div[4]/div/div/a[' + str(page + 3) + ']').click()
        for model in range(1, 61):  # 페이지 모델별
            print('model : ',model)
            # driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/div[4]/div/ul/li[1]')
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/div[4]/div/ul/li[' + str(model) + ']').click()  # 모델 60
            time.sleep(1)
            imgUrl = driver.find_element_by_xpath('//*[@id="style_info"]/div[2]/div[2]/div/div/img[2]').get_attribute('src')
            with urlopen(imgUrl) as f:

                if count<3:
                    with open('./woman_data/'+str(page+1)+'-'+str(model)+'.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                        img = f.read()  # 이미지 읽기
                        h.write(img)
                else:
                    with open('./man_data/'+str(page+1)+'-'+str(model)+'.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                        img = f.read()  # 이미지 읽기
                        h.write(img)

            temp = []

            for c in range(1, 4):  # 3개의 아이템만 가져오겠다. 왜냐하면 대부분 상하의는 3개선에서 끝 & tap 띄어서 크롤링 드리블 하기
                if not (driver.find_elements_by_xpath(
                        '//*[@id="style_info"]/div[3]/div[2]/div/div/div[1]/div[' + str(c) + ']/a[2]')):
                    temp.append(np.nan)
                    temp.append(np.nan)
                else:
                    temp.append(driver.find_element_by_xpath(
                        '//*[@id="style_info"]/div[3]/div[2]/div/div/div[1]/div[' + str(c) + ']/a[2]').text)
                    driver.find_element_by_xpath(
                        '//*[@id="style_info"]/div[3]/div[2]/div/div/div[1]/div[' + str(c) + ']/a[2]').send_keys(
                        Keys.COMMAND + '\n')
                    driver.find_element_by_xpath('//*[@id="style_info"]/div[3]/div[2]/div/div/div[1]/div[1]/a[2]')
                    driver.switch_to.window(driver.window_handles[1])
                    temp.append(
                        driver.find_element_by_xpath('//*[@id="page_product_detail"]/div[3]/div[3]/div[1]/p/a[2]').text)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            driver.back()
            if sex == 0:
                stylist_data['여자 ' + str(page) + '번 page ' + str(model) + '번 model'] = temp
            if sex == 1:
                stylist_data['남자 ' + str(page) + '번 page ' + str(model) + '번 model'] = temp

stylist_data.to_csv('stylist_table.csv', encoding='utf-8-sig')
