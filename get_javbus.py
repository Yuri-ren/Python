# coding: utf-8
import requests
from bs4 import BeautifulSoup


# 当前girl全量页面
def get_fh_section(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    print(soup)



if __name__ == "__main__":
    get_fh_section('https://www.javbus.com/star/2eg')
    print("你好")
