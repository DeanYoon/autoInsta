from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import random
import openpyxl
import pandas as pd
import platform
import getpass
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# Get the operating system's name
os_name = platform.system()
username = getpass.getuser()

# Print the operating system's name






#로그인


def login(BOT_ID,BOT_PASSWORD):
    driver.find_element(by=By.TAG_NAME, value="input").send_keys(BOT_ID)
    driver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys(BOT_PASSWORD)
    time.sleep(10+random.randint(3,5))
    driver.find_elements(by=By.TAG_NAME, value="input")[1].send_keys(Keys.ENTER)
    time.sleep(10+random.randint(5,10))



#click first image
def click_image(i):
    photos_box = driver.find_elements(by=By.CLASS_NAME, value='_aabd')
    photos_box[i].click()
    time.sleep(10+random.randint(5,10))
# click_image(8)

# #Go to User Profile
# userID = driver.find_element(by=By.CLASS_NAME, value='_acaw')
# userID.click()
# time.sleep(10+5)


#check if follow state at user profile
def check_follow_state_follow():
    follow_state = driver.find_element(by=By.CLASS_NAME, value='_aacw')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    follow_state = soup.find(class_='_aacl _aaco _aacw _aad6 _aade').text

    if  follow_state =='팔로우':
        #Follow
        follow_btn = driver.find_element(by=By.CLASS_NAME, value='_acan')
        follow_btn.click()
        time.sleep(10+random.randint(3,8))

# 메세지 버튼 클릭 xsz8vos
def click_message_btn():
    message_btn = driver.find_element(by=By.CLASS_NAME, value='xsz8vos')
    time.sleep(10+2+random.random()*10)
    message_btn.click()
    time.sleep(10+7+random.random()*10)


#input box

def send_messages(ms1,ms2,ms3,ms4):
    dm_input = driver.find_element(by=By.CSS_SELECTOR, value=".x1n2onr6 [role='textbox']")
    dm_input.send_keys(ms1,Keys.ENTER)
    time.sleep(10+random.random()*10)
    dm_input.send_keys(ms2,Keys.ENTER)
    time.sleep(10+random.random()*10)
    dm_input.send_keys(ms3,Keys.ENTER)
    time.sleep(10+random.random()*10)
    #get_images_send()
    #time.sleep(10+8+random.random()*10)
    dm_input.send_keys(ms4,Keys.ENTER)



def get_images_send():
    files = os.listdir('./images')
    image_files = []

    for file in files:
        if file.endswith(('png', 'jpg', 'jpeg','gif')):
            image_files.append(file)
        
        
    #파일 복사
    folder_path = "./images"
    os.system("open " + folder_path + '/'+image_files[random.randint(0,len(image_files)-1)])
    time.sleep(10+2+random.random()*10)

    #copy
    if os_name == 'Darwin':
        pyautogui.hotkey('command','c',pause=0.5)
        input_elem = driver.find_element(by=By.CSS_SELECTOR, value=".x1n2onr6 [role='textbox']")
        input_elem.send_keys(Keys.COMMAND + 'v')
    elif os_name == 'Window':
        pyautogui.hotkey('ctrl','c',pause=0.5)
        input_elem = driver.find_element(by=By.CSS_SELECTOR, value=".x1n2onr6 [role='textbox']")
        input_elem.send_keys(Keys.CTRL + 'v')
    #paste img


    input_elem.send_keys(Keys.ENTER)
    try:
        driver.find_elements(by=By.CLASS_NAME, value='xzloghq')[0].click()
    except:
        pass
        
    time.sleep(10+2+random.random()*10)









#코멘트 단 사람들의 유저 아이디 가져와서 기존 데이터에 추가
def get_comment_ids_from_photo(data):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    message_ids = soup.find_all(class_='_a9zc') # 각 아이디를 담고 있는 태그

    for id in message_ids:
        user_id = id.find('a').text

        if  user_id not in data:
            data.append(id.find('a').text)


    return data

# added_user_data = get_comment_ids_from_photo(user_data)



# save to excel
def save_user_id_excel(added_data):
    wb = openpyxl.Workbook()
    ws = wb.active
    for data in added_data:
        ws.append([data])

    # save the workbook
    wb.save(f'/Users/{username}/Downloads/automate/userList.xlsx')
    
# save_user_id_excel(added_user_data)





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


def open_chrome(PROXY):
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL"
    }

    driver = webdriver.Chrome(chromedriver_path)

    driver.get("https://www.google.com/")
    return driver



def proxy_login(proxy_username,proxy_password):
    pyautogui.typewrite(proxy_username)
    pyautogui.press("tab")
    pyautogui.typewrite(proxy_password)
    pyautogui.press("enter")


    
    
def move_to_user_follow_btn():
    user_data = pd.read_excel(f'/Users/{username}/Downloads/automate/userList.xlsx', sheet_name='Sheet').values.tolist()
    user_data = list(map(lambda x: x[0], user_data))
    driver.get(f"https://www.instagram.com/{user_data[random.randint(0,len(user_data))]}")
    time.sleep(10+random.randint(10,15))
    try:
        driver.find_element(By.XPATH, '//div[@aria-label="모든 쿠키 허용"]').click()
        time.sleep(10+3+random.random()*10)
    except:
        pass
    
    
    try:
        check_follow_state_follow()
    except:
        pass





def get_message_send_random():

    chat_datas = pd.read_excel(f'/Users/{username}/Downloads/automate/data.xlsx', sheet_name='DM')
    message1 = chat_datas.iloc[:,0].tolist()
    message2 = chat_datas.iloc[:,1].tolist()
    message3 = chat_datas.iloc[:,2].tolist()
    message4 = chat_datas.iloc[:,3].tolist()
    max_num = len(message1)-1
    rand_msg1,rand_msg2,rand_msg3,rand_msg4 =  message1[random.randint(0,max_num)],message2[random.randint(0,max_num)],message3[random.randint(0,max_num)],message4[random.randint(0,max_num)]

    send_messages(rand_msg1,rand_msg2,rand_msg3, rand_msg4)
    
    


def get_message_send_random_ver2():
    chat_datas = pd.read_excel(f'/Users/{username}/Downloads/automate/data.xlsx', sheet_name='DM')
    message1 = chat_datas.iloc[:,0].tolist()
    message2 = chat_datas.iloc[:,1].tolist()
    message3 = chat_datas.iloc[:,2].tolist()
    message4 = chat_datas.iloc[:,3].tolist()
    max_num = len(message1)-1
    rand_msg1,rand_msg2,rand_msg3,rand_msg4 =  message1[random.randint(0,max_num)],message2[random.randint(0,max_num)],message3[random.randint(0,max_num)],message4[random.randint(0,max_num)]
    
    
    dm_input = driver.find_element(by=By.TAG_NAME, value='textarea')
    dm_input.send_keys(rand_msg1,Keys.ENTER)
    time.sleep(10+3)
    dm_input.send_keys(rand_msg2,Keys.ENTER)
    time.sleep(10+3)
    dm_input.send_keys(rand_msg3,Keys.ENTER)
    time.sleep(10+3)
#이미지 전송
#     files = os.listdir('./images')
#     image_files = []

#     for file in files:
#         if file.endswith(('png', 'jpg', 'jpeg','gif')):
#             image_files.append(file)
        
#     #파일 복사
#     folder_path = "./images"
#     os.system("open " + folder_path + '/'+image_files[random.randint(0,len(image_files)-1)])
#     time.sleep(10+2)

    
    
#     #copy
#     if os_name == 'Darwin':
#         pyautogui.hotkey('command','c',pause=0.5)
#         input_elem = driver.find_element(by=By.TAG_NAME, value='textarea')
#         input_elem.send_keys(Keys.COMMAND + 'v')
#     elif os_name == 'Window':
#         pyautogui.hotkey('ctrl','c',pause=0.5)
#         input_elem = driver.find_element(by=By.TAG_NAME, value='textarea')
#         input_elem.send_keys(Keys.CTRL + 'v')
#     else:
#         print('inValid os')
#     #사진 submit
#      try:
#         driver.find_elements(by=By.CLASS_NAME, value='xzloghq')[0].click()
#     except:
#         pass
#     try:
#         driver.find_element(by=By.CLASS_NAME, value='_acap').click()
#     except:
#         pass
#     time.sleep(10+2)
#     dm_input.send_keys(rand_msg4,Keys.ENTER)
    time.sleep(10+5)

    



from selenium import webdriver

num = 0
fail = 0
#main


login_datas = pd.read_excel(f'/Users/{username}/Downloads/automate/data.xlsx', sheet_name='Login').values.tolist()
chromedriver_path = "./chromedriver"

for t in range(20):
    for i in range(len(login_datas)):
        user_id,user_password,proxy_username,proxy_password,PROXY = get_login_data(i)
        
        # Create a new Chrome webdriver instance
        driver = webdriver.Chrome(chromedriver_path)
        time.sleep(10+3)
        driver.get("https://www.instagram.com/")
        time.sleep(10+15+random.random()*10)
        try:
            driver.find_element(by=By.CLASS_NAME, value='_a9_0').click()
            time.sleep(10+5+random.random()*10)
        except:
            pass
        
        try:
            login(user_id, user_password)
            for j in range(5):
                move_to_user_follow_btn()
                try:
                    click_message_btn()
                    try:#알림설정
                        driver.find_element(by=By.CLASS_NAME, value='_a9_1').click()
                        time.sleep(10+3+random.random()*10)
                    except:
                        pass

                    try:
                        get_message_send_random()
                        num+=1
                        print(num,' done')
                    except:
                        try:
                            get_message_send_random_ver2()
                            num+=1
                            print(num, ' done')
                        except:
                            print('메세지 불가 계정')
                            fail+=1
                            pass


                except:
                    print('비공개 계정')
                    fail+=1
                    pass
#                 time.sleep(10+random.random()*15+10)
            driver.quit()

        except:
            print("Login Failed")
            pass
        print(f'success : {num}, fail : {fail}')