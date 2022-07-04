from bs4 import BeautifulSoup
import requests, urllib.parse
import re
from config import *
import os
import aspose.words as aw
from urllib.error import HTTPError

match_keyword_for_neem = "Neem"

def click_url(url,data):
    collected = ''
    try:
        response = requests.get(url,headers=headers).text
    except:
        pass
    else:
        print("it's worked")
        response = requests.get(url,headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')
    get_len = len(soup.find_all('h2'))
    if get_len > 0:
        all_h2_tag = [i.text.lower() for i in soup.find_all('h2')]
        print(all_h2_tag,"====")
        for item in all_h2_tag:
            if data.lower() in item:
                collected = item
                paragraph = [i.text for i in soup.find_all("p")]
                # document_create(collected)
                # print(paragraph)
            else:
                pass
        return collected,True
    else:
        return "[INFO] Goto next page..", False


def paginate(url,data ,previous_url=None):
    if url == previous_url: return
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all('div', class_='yuRUbf')
    for link in links:
        title = link.find('h3', text=re.compile(match_keyword_for_neem))
        if title != None:
            get_title = title.text
        get_links = link.find('a')
        show_url_list = get_links.get('href')
        print("[INFO] WORKING ON URL : ",show_url_list)

        datas,status = click_url(show_url_list,data)
        # print(status,"=+++==")
        print(datas,"====")
        if status:
            print(datas,end='\n')
        else:
            print("[INFO] ",show_url_list,"\nURL having 0 H2")
            print(datas,end='\n')
        emp_list.append(show_url_list)

    yield soup
    next_page_node = soup.select_one('a#pnnext')
    if next_page_node is None: return
    next_page_url = urllib.parse.urljoin('https://www.google.com/',next_page_node['href'])
    yield from paginate(next_page_url,data, url)

def scrape(data):
    text = input('Enter the text that you want to search.......\n')
    pages = paginate('https://google.com/search?q='+text,data)
    for soup in pages:
        count_page = int(soup.select_one(".YyVfkd").text)
        if count_page == 4:
            break


def document_create(write_file):
    file = 'Neem.docx'
    path = os.path.abspath(file)
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    builder.write(write_file)
    doc.save(path)

def main():
    data = search_data
    for i in data:
        get_keyword = i.get('matchkeyword')
        for show in get_keyword:
            show_all_keyword = show
            scrape(show_all_keyword)
emp_list  = list()

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
main()
