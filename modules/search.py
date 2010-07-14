#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#
"""
search.py - lokky search module
Copyright 2008, Claudio Borges
Licensed under BSD License.
"""
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

class Search(object):

    def __init__(self, qtde=3):
        self.qtde = qtde
        self.base_url = { 'google': 'http://www.google.com.br', 'youtube': 'http://www.youtube.com', 'maplink': 'http://maplink.uol.com.br' }

    def get_html(self, u):
        self.header = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1'
        self.conn = Browser()
        self.conn.addheaders = [('User-agent', self.header)]
        self.conn.set_handle_robots(False)
        self.conn.open(u)
        self.page = self.conn.response().read()
        return BeautifulSoup(self.page)

    def google(self, s):
        search = "/search?source=ig&hl=pt-BR&rlz=&q=%s&btnG=Pesquisa+Google&meta=" % s.replace(' ', '+')
        url = self.base_url['google'] + search
        try:
            soup = self.get_html(url)
            result = soup.findAll('div', attrs={'id': 'res'})[0].findAll('li', attrs={'class': 'g'})
            urls = []
            if len(result) > 0:
                for link in result[0:self.qtde]:
                    urls.append(link.h3.a['href'])
                return urls
            else:
                urls.append("nenhum resultado encontrado para %s" % s)
                return urls
        except:
                urls.append("erro na consulta, nao consegui fazer o parse para %s" % s)
                return urls

    def youtube(self, s):
        search = "/results?search_query=%s&aq=f" % s.replace(' ', '+')
        url = self.base_url['youtube'] + search
        try:
            soup = self.get_html(url)
            result = soup.findAll('div', attrs={'class': 'video-long-title'}, limit=self.qtde)
            urls = []
            if len(result) > 0:
                for link in result:
                    urls.append(self.base_url['youtube'] + link.a['href'])
                return urls
            else:
                urls.append("nenhum resultado encontrado para %s" % s)
                return urls
        except:
                urls.append("erro na consulta, nao consegui fazer o parse para %s" % s)
                return urls

    def maplink(self):
        url = "http://maplink.uol.com.br/v2/corredores/Sao-Paulo-SP.htm"
        soup = self.get_html(url)
        var = soup.find('ul', id="ctl00_ctl00_cphConteudo_cphConteudo_ulResumoCondicao").findAllNext(text=True, limit=7)
        t = ""
        for x in var:
            t +=  " " + x.encode('utf-8').strip()
        return t.strip()
