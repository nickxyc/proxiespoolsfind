from spider import Spider

def main():
    url = 'https://www.kuaidaili.com/free/'
    spider_one = Spider()
    page_source = spider_one.html_get(url=url)
    tarlist = spider_one.analysis_html_page(page_source)
    proxys = spider_one.deal_list(tarlist)
    spider_one.save_data_base(proxys)

if __name__ == '__main__':
    main()