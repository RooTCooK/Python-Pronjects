import scrapy

# 验证完毕，可以导入items类进行类实例化传输结果
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoztools.net']
    # 限定爬虫访问的域名，防止范围过于宽泛
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        # 测试爬虫可以正常爬取网页代码，合并保存下来
        # filename = response.url.split('/')[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # 接下来开始使用 xpath 对代码进行筛选，得到自己想要的内容
        sel = scrapy.selector.Selector(response)
        items = []
        sites = sel.xpath(
            '//div/div[@class="title-and-desc"]')
        for site in sites:
            # 下面的验证爬虫正常工作，打印出来需要的内容，之后就可以传入实例化的item
            # title = site.xpath('a/div/text()').extract()
            # link = site.xpath('a/@href').extract()
            # desc = site.xpath('div/text()').extract()
            # print(title, link, desc)
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)
        return items
