import requests
from bs4 import BeautifulSoup
import re
import checkDownloaded
import WorkInTime
import account

def Get_Session(URL,DATA,HEADERS):
    '''保存登录参数'''
    ROOM_SESSION  = requests.Session()
    ROOM_SESSION.post(URL,data=DATA,headers=HEADERS)
    return ROOM_SESSION

def loginAndDownload():  # 登陆函数

    header = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Origin':'http://www.zimuzu.tv',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    url = 'http://www.zimuzu.tv/User/Login/ajaxLogin'

    login_session = requests.Session()
    login_session.post(url,
           data=account.postData233,
           headers=header)
    _cookies = (login_session.cookies)
    #print(login_session.status_code)
    #print(_cookies.get_dict())
    url = 'http://www.zimuzu.tv/user/fav'
    f = login_session.get(url)
    #print(f.content.decode())

    soup = BeautifulSoup(f.content.decode(), "html.parser")
    #print(soup.prettify())

    # 第一次运行添加这两个文件
    file_object = open(r'D:\pythonResouce\mj.txt', 'a')
    fileNewDownload = open(r'D:\pythonResouce\newmj.txt', 'a')
    for link in soup.find_all(href=re.compile("ed2k")):
        #print(type(link))
        #print(link.attrs)
        #print(link['href'])
        if link['href'] not in downloaded:
            print(link['href'])
            file_object.write(link['href']+'\n')
            fileNewDownload.write(link['href']+'\n')
    file_object.close()
    fileNewDownload.close()
    print('well done')

timeBucket =[['11:30']*2]

workTime = WorkInTime.WorkInTime(timeBucket)
print("追剧正在进行")
while True:
    downloaded = checkDownloaded.checkDownloaded()
    loginAndDownload()
    workTime.relax()
