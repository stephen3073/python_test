# author：wyf927
'''
    1。请求数据，发送http请求获取数据
    2。解析数据，以正确的格式
    3，保存数据
'''
# https://www.xsbiquge.com/20_20331/
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
def getcontent(target):
    req=requests.get(url=target)
    req.encoding="utf-8"
    html=req.text
    # 解析数据
    bs=BeautifulSoup(html,"lxml")
    texts=bs.find('div',id='content')
    #print(texts)
    texts_2=texts.text.strip().split('\xa0'*4)
    return texts_2
if __name__=="__main__":
    # 获取数据
    # target='https://www.xsbiquge.com/20_20331/1135932.html'
    server="https://www.xsbiquge.com/20_20331/"
    target="https://www.xsbiquge.com"
    # 章节列表
    bookname="11"
    req = requests.get(url=server)
    req.encoding = "utf-8"
    html = req.text
    # 解析数据
    chapter_bs = BeautifulSoup(html, "lxml")
    chapters = chapter_bs.find("div",id="list")
    chapters=chapters.find_all("a")
    for chapter in tqdm(chapters):
        chapter_name=chapter.string
        print(chapter.get('href'))
        url=target+chapter.get('href')
        print(url)
        # https://www.xsbiquge.com/20_20331/1135932.html
        content = getcontent(url)
        with open(bookname,'a',encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')









    # 获取每个章节链接


