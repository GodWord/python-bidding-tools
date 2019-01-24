# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/1/17 10:13'

import requests

from utils.CrawlerUtils import CrawlerUtils


class Szzfcg:
    url = 'http://www.szzfcg.cn/portal/topicView.do?method=view&id=2719966'

    data = {
        'ec_i': 'topicChrList_20070702',
        'topicChrList_20070702_crd': 20,
        'topicChrList_20070702_f_a': '',
        'topicChrList_20070702_p': 1,
        'topicChrList_20070702_s_siteId': '',
        'topicChrList_20070702_s_name': '',
        'topicChrList_20070702_s_speciesCategory': '',
        'id': '2719966',
        'method': 'view',
        '__ec_pages': '1',
        'topicChrList_20070702_rd': 20,
        'topicChrList_20070702_f_name': '',
        'topicChrList_20070702_f_speciesCategory': '',
        'topicChrList_20070702_f_ldate': '',
    }

    @staticmethod
    def get_html(i):
        Szzfcg.data['topicChrList_20070702_p'] = i
        headers = {
            'User-Agent': CrawlerUtils.get_user_agent()
        }
        req = requests.post(Szzfcg.url, data=Szzfcg.data, headers=headers)
        html = req.text
        return html

    @staticmethod
    def run():
        headers = {
            'User-Agent': CrawlerUtils.get_user_agent()
        }
        req = requests.post(Szzfcg.url, data=Szzfcg.data, headers=headers)
        html = req.text

        total_count = int(CrawlerUtils.get_tag(html, 'td.statusBar')[0].text.split(',')[0][2:-3])
        page = 1
        count = 0
        while True:
            html = Szzfcg.get_html(page)
            tr_tags = CrawlerUtils.get_tag(html, 'tbody.tableBody tr')
            for i in tr_tags:
                count += 1
                content = i.contents
                print(content[3].text.strip())
                print(content[5].text.strip())
                print(content[9].text.strip())
                print(count)
                print('======================================================================')

            if total_count <= page * Szzfcg.data['topicChrList_20070702_crd']:
                break
            page += 1
