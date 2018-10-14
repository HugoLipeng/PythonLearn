#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


# 获取url下的页面内容
def get_pages(link_url):
    response = requests.get(link_url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# 获取链接列表
def get_links(link_url):
    response = requests.get(link_url)
    soup = BeautifulSoup(response.text,'lxml')
    links_div = soup.find_all('div', class_='pic_panel')

    links = [div.a.get('href') for div in links_div]
    return links

link_url = 'https://wh.lianjia.com/zufang/'
get_pages(link_url)
get_links(link_url)