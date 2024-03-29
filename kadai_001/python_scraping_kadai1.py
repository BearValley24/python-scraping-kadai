# -*- coding: utf-8 -*-
"""python-scraping-kadai1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1er3q2GeA-aurZe85AcTKZ76DGpcArcks
"""

# 対象サイトを取得
#!pip install requests

import requests
url = 'https://news.yahoo.co.jp/articles/a12fab12de72e183c5562e11e78279a007c871e6'
response = requests.get(url)
html = response.text

# 対象サイトのHTMLを解析
#!pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 対象のサイトのニュース本分のp要素は同じclass名で2つある
# findは最初に見つかった要素のみを表示、find_allは全てを表示
# https://pystyle.info/scraping-beautiful-soup-how-to-find-elements/#outline__5_1
p_tag = soup.find_all('p', class_='sc-lhuRmv fFWOLV yjSlinkDirectlink highLightSearchTarget')

# テキストのみを表示
p_text0 = p_tag[0].text
p_text1 = p_tag[1].text
print(p_text0, p_text1)