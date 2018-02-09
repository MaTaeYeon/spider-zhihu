import scrapy
from scrapy.http import Request
import time
from selenium import webdriver
from zhihu.items import ArticleItem
from lxml import html
from bs4 import BeautifulSoup

class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = [
        "https://www.zhihu.com/people/xiao-xiao-ying-65-55/posts"
    ]

    def parse(self, response):
        browser = webdriver.Firefox(executable_path='C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
        browser.get(response.url)
        time.sleep(2)
        #敲开所有的文章
        for i in range(0, len(browser.find_elements_by_class_name("RichContent-inner"))):
            browser.find_elements_by_class_name("RichContent-inner")[i].click()
        time.sleep(10)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        browser.quit()

        articles = soup.select('div[class="List-item"]')
        for article in articles:
            nickname = article.select('meta[itemprop="name"]')[0].get('content')
            avatar = article.select('img[class="Avatar AuthorInfo-avatar"]')[0].get('src')
            title = article.select('h2[class="ContentItem-title"] a')[0].string
            link = self.start_urls[0]
            #cover有两种
            try:
                cover = article.select('div[class="VagueImage ArticleItem-image"]')[0].get('data-src')
            except:
                cover = article.select('img[class="ArticleItem-image"]')[0].get('src')
            img_list = cover
            content_str = str(article.select('div[class="RichContent"]')[0])
            tag_str = ''
            publish_date = self.get_strftime()
            url = response.url

            item = ArticleItem()
            item['nickname'] = nickname
            item['avatar'] = avatar
            item['title'] = title
            item['link'] = link
            item['cover'] = cover
            item['img_list'] = img_list
            item['content_str'] = content_str
            item['tag_str'] = tag_str
            item['publish_date'] = publish_date
            item['url'] = url
            yield item

    def get_strftime(self):
        # 获取当前时间
        time_now = int(time.time())
        # 转换成localtime
        time_local = time.localtime(time_now)
        # 转换成新的时间格式(2016-05-09 18:59:20)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt