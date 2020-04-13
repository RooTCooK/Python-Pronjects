import scrapy
import urllib.request
import urllib.parse
import re
from dagushu.items import DagushuItem

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
    return re.findall(p, html[aim:aim+300])[0]

# 根据link网址，得到具体的下载链接
def downMp3(downURL, title):
    # response.xpath('//div[@class="download_link"]/a[@class="input"]/@href').extract()
    req = urllib.request.Request(downURL)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urllib.request.urlopen(downURL)
    m4a = response.read()
    with open(title, 'wb') as f:
        f.write(m4a)
    # for site in sites:
    #     print(site)

class DaguSpider(scrapy.Spider):
    name = "dagu"
    allowed_domains = ['fl5y.com']
    start_urls = [
        'http://www.fl5y.com/xiazai/dagushu/'+str(x)+'.html' for x in range(7934,8399)] #6212-8400

    def parse(self, response):
        # 测试爬虫可以正常爬取网页代码，合并保存下来
        # filename = response.url.split('/')[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        sel = scrapy.selector.Selector(response)
        items = []
        item = DagushuItem()
        item['title'] = sel.xpath('//div/p/a/text()').extract()[0]
        item['link'] = sel.xpath('//audio/source/@src').extract()[0]
        items.append(item)
        # print(item)
        print(item['link'])
        # print(urllib.parse.quote(item['link']))
        # downURL = getDownUrl(item['link'])
        # print(downURL)
        # print(urllib.parse.urlencode(downURL))
        downMp3(item['link'], 'E:\\dagu\\'+item['title']+".mp3")
