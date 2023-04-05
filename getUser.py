#get ids
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import openpyxl
import pandas as pd
import getpass
import sys
import threading
import numpy as np
def getUser_thread():
    def click_image(i):
        photos_box = driver.find_elements(by=By.CLASS_NAME, value='_aabd')
        photos_box[i].click()
        time.sleep(random.randint(5,10))

    def get_comment_ids_from_photo(data):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        message_ids = soup.find_all(class_='_a9zc') # 각 아이디를 담고 있는 태그

        for id in message_ids:
            user_id = id.find('a').text

            if  user_id not in data:
                data.append(id.find('a').text)


        return data

    def save_user_id_excel(added_data):
        result_list = [np.nan]*len(added_data)
        data = {'Username':added_data, 'Result':result_list}
        df = pd.DataFrame(data)
        # save the workbook
        df.to_excel(f'/Users/{username}/Downloads/automate/userList.xlsx', index=False)
        time.sleep(2)



    def get_login_data(i):
        user_data = (login_datas[i])# N번째 계정
        user_id = user_data[0]
        user_password = user_data[1]
        user_proxy = user_data[2]
        user_port = int(user_data[3])
        proxy_username = user_data[4]
        proxy_password = user_data[5]
        PROXY = f'{user_proxy}:{user_port}'
        return user_id,user_password,proxy_username,proxy_password,PROXY


    def login(BOT_ID,BOT_PASSWORD):
        driver.find_element(by=By.TAG_NAME, value="input").send_keys(BOT_ID)
        driver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys(BOT_PASSWORD)
        time.sleep(random.randint(3,5))
        driver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys(Keys.ENTER)
        time.sleep(random.randint(5,10))



    username = getpass.getuser()

    hashtag = pd.read_excel(f'/Users/{username}/Downloads/automate/data.xlsx', sheet_name='Tag').values.tolist()
    hashtag = list(map(lambda x: x[0], hashtag))


    login_datas = pd.read_excel(f'/Users/{username}/Downloads/automate/data.xlsx', sheet_name='Login').values.tolist()
    user_id,user_password,proxy_username,proxy_password,PROXY = get_login_data(1)
    chromedriver_path = "./chromedriver"
    driver = webdriver.Chrome(chromedriver_path)
    time.sleep(3)
    driver.get("https://www.instagram.com/")
    time.sleep(15+random.random()*10)


    try:
        driver.find_element(by=By.CLASS_NAME, value='_a9_0').click()
        time.sleep(5+random.random()*10)
    except:
        pass

    login(user_id, user_password)
    time.sleep(10)

    for i in range(len(hashtag)):
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag[i]}")
        time.sleep(10)
        for j in range(9):
            click_image(j)
            #저장한 유저 아이디 불러오기
            try:
                data = pd.read_excel(f'/Users/{username}/Downloads/automate/userList.xlsx', sheet_name='Sheet1')
                if len(data) > 300:
                    sys.exit()
            except:
                user_data = []
            #2D 에서 1D
            user_data = data.iloc[:,0].tolist()
            added_user_data = get_comment_ids_from_photo(user_data)
            save_user_id_excel(added_user_data)
            print("Saved id number : ", len(added_user_data))
            driver.back()
            
def getUser():
    t = threading.Thread(target=getUser_thread)
    t.start()
