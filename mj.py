import requests
from bs4 import BeautifulSoup
import re
import checkDownloaded
import account
import WorkInTime

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Language': 'zh-CN;q=0.01',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Tablet PC 2.0)',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zmz2017.com',
    'DNT': '1'
}

def loginAndDownload():  # 登陆函数

    url = 'http://www.zmz2017.com/User/Login/ajaxLogin'
    # postData like this
    postData = {
        'account': '*',
        'password': '******',
        'remember': '1'
    }

    login_seesion = requests.Session()
    login_seesion.post(url,
                       data=account.postData,
                       headers=header)

    url = 'http://www.zmz2017.com/user/fav'
    f = login_seesion.get(url, headers=header)
    #print(f.content.decode())

    soup = BeautifulSoup(f.content.decode(), "html.parser")
    #print(soup.prettify())

    # 第一次运行添加这两个文件
    file_object = open('D:/pythonResouce/mj.txt', 'a')
    fileNewDownload = open('D:/pythonResouce/newmj.txt', 'a')
    for link in soup.find_all(href=re.compile("ed2k")):
        #print(type(link))
        #print(link.attrs)
        if link['href'] not in downloaded:
            print(link['href'])
            file_object.write(link['href']+'\n')
            fileNewDownload.write(link['href']+'\n')
    file_object.close()
    fileNewDownload.close()
    print('well done')

timeBucket =[['12:30']*2]
workTime = WorkInTime.WorkInTime(timeBucket)
print("追剧正在进行")
while True:
    downloaded = checkDownloaded.checkDownloaded()
    loginAndDownload()
    workTime.relax()