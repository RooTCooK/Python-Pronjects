import urllib.request
import urllib.parse
import os
import requests
import re
url = 'http://www.mediafire.com/file/sm86qy48xldosmn/www.for1.mp3'

# req = urllib.request.Request(url)
# req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8')
# # print(html)
# response.close()

# # 查找网址，并保存下来网页
# # aim = html.find('<a class="input"')
# # print(aim)
# # print(html[aim:aim+200])
# # with open('1111.html', 'w') as f:
# #     f.write(html)

# # 因为正则表达式中"."不能匹配换行符，所以无法匹配到数据
# aim = html.find('<a class="input"')
# p = r'href="(.+?\.mp3)"'
# downUrl = re.findall(p, html[aim:aim+300])

def downMp3(downURL, title):
    # response.xpath('//div[@class="download_link"]/a[@class="input"]/@href').extract()
    req = urllib.request.Request(downURL)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(downURL)
    print(response.getheaders())
    resContent = response.read()
    with open(title, 'wb') as f:
        f.write(resContent)

# 接下来把上面的测试结果包装起来
def getDownUrl(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    response.close()
    aim = html.find('<a class="input"')
    p = r'href="(.+?\.mp3)"'
    # downUrl = re.findall(p, html[aim:aim+300])
    return re.findall(p, html[aim:aim+300])


def DownloadFile(mp3_url, save_url,file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        res = requests.get(mp3_url,stream=True)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name+' 成功下载！')
    except:
        print("程序错误")

if __name__ == "__main__":
    # MP3源地址url
    url = 'http://download698.mediafire.com/ca353e29my8g/pyoaec639mjb3v7/0469%28www.fl5y.com%29.mp3'
    # MP3保存文件夹
    save_url='./'
    # MP3文件名
    file_name = 'mymusic.mp3'
    DownloadFile(url,save_url, file_name)

# downurllll = 'http://download698.mediafire.com/ca353e29my8g/pyoaec639mjb3v7/0469%28www.fl5y.com%29.mp3'
# print(urllib.parse.unquote(downurllll))
# downMp3(urllib.parse.unquote(downurllll), '222222.mp3')