#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 爬虫前奏
#
# 明确目的
# 找到数据相应的网页
# 分析网页的结构找到数据所在的标签位置
#
# 模拟HTTP请求，向服务器发送请求，获取服务器返回给我们的HTML
# 用正则表达式提取我们要的数据（名字，人气）

from urllib import request


class Spider():
     url ='https://www.panda.tv/cate/lol'
     root_pattern = '<div class="video-info">([\s\S]*?)</div>'
     name_pattern = '</i>([\s\S]*?)</span>'
     number_pattern = '<span class="video-number">([\s\S]*?)</span>'

     def __fetch_content(self):
         r = request.urlopen(Spider.url)
         htmls = r.read()
         htmls = str(htmls,encoding='utf-8')
         return htmls

     def __analysis(self,htmls):
         root_html = request.findall(Spider.root_pattern.htmls)
         anchors = []
         for html in root_html:
             name = request.findall(Spider.name_pattern,html)
             number = request.findall(Spider.number_pattern,html)
             anchor = {'name':name,'number':number}
             anchors.append(anchor)
         print(anchors[0])
         return anchors

     def __refine(self,anchors):
         l = lambda anchor:{
             'name':anchor['name'][0].strip(),
             'number':anchors['number'][0]
         }
         return map(l,anchors)

     # def __sort(self,anchors):

     def go(self):
         htmls = self.__fetch_content()
         anchors = self.__analysis(htmls)
         anchors =list(self.__refine(anchors))
         print(anchors)


spider = Spider()
spider.go()






















