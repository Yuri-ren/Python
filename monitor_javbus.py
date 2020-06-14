# coding: utf-8

import json
import requests

from bs4 import BeautifulSoup

av_girl_url = 'https://www.javbus.com/star/qs6'
girl_page_list = []

req = requests.get(av_girl_url)
print(req.status_code)


