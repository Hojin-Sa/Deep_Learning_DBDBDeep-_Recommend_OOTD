from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlopen
import time


driver = webdriver.Chrome(
    executable_path= './chromedriver'
)

for cnt in range(2):
    url = "https://store.musinsa.com/app/styles/lists?source=M_MUSINSA_NEWS/"
    driver.get(url)
    action = ActionChains(driver)
    driver.find_element_by_xpath('//*[@id="default_top"]/div[2]/button['+str(cnt+2)+']').send_keys(Keys.ENTER)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tmp_j = 0
    tmp_i = 0

    for i in range(3,13):
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[3]/form/div[4]/div/div[4]/div/div/a[' + str(i + 3) + ']').click()

        for j in range(1,61):
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/form/div[4]/div/ul/li[' + str(j) + ']').click()  # 모델 60
            imgUrl = driver.find_element_by_xpath('//*[@id="style_info"]/div[2]/div[2]/div/div/img[2]').get_attribute('src')
            with urlopen(imgUrl) as f:
                tmp_j = j - 15
                tmp_i = i

                if tmp_j < 1:
                    tmp_i-=1
                    tmp_j+=60

                if cnt==0:
                    with open('./woman_data/'+str(tmp_i-2)+'-'+str(tmp_j)+'.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                        img = f.read()  # 이미지 읽기
                        h.write(img)
                else:
                    with open('./man_data/'+str(tmp_i-2)+'-'+str(tmp_j)+'.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                        img = f.read()  # 이미지 읽기
                        h.write(img)
            driver.back()