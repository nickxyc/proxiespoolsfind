from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import lxml
import pymongo
class Spider():

    def __init__(self):
        pass
    def html_get(self,url):
        """
        传入目标网页的url
        :return:网页的源数据
        """
        try:
            browser = webdriver.Chrome()
            browser.get(url)
            wait = WebDriverWait(browser,10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#list > table > tbody")))
            return browser.page_source
        except TimeoutException:
            self.html_get(url)
        finally:
            browser.quit()

    def analysis_html_page(self,page_source):
        soup = BeautifulSoup(page_source,"lxml")
        return soup.find_all(name="tr")
    def deal_list(self,lists):
        del lists[0]

        proxys = []
        for tag in lists:
            childlist =[]
            for child in tag.children:
                childlist.append(child)
            proxy = {
                'IP':childlist[1].string,
                'PORT':childlist[3].string,
                '匿名度':childlist[5].string,
                '类型':childlist[7].string,
                '位置':childlist[9].string,
                '响应速度':childlist[11].string,
                '最后验证时间':childlist[13].string

            }
            proxys.append(proxy)
        return proxys
    def save_data_base(proxies)
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client.proxiespools
        collection = db.proxies
        for proxy in proxies
        collection.insert(proxy)
