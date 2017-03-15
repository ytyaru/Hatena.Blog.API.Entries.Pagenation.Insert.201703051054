#!python3
#encoding:utf-8
import xmltodict
from collections import OrderedDict
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
import datetime
import xml.sax.saxutils
import html
import dataset
from urllib.parse import urlparse
import re

class Inserter(object):
    def __init__(self, path_hatena_entries_sqlite3):
        self.db_entries = dataset.connect('sqlite:///' + path_hatena_entries_sqlite3)
            
    def insert_entry(self, entry, entry_id):
        if (None == self.db_entries['Entries'].find_one(EntryId=entry_id)):
            self.db_entries['Entries'].insert(dict(
                EntryId=entry_id,
                Url=entry.find('link', rel='alternate').get('href'),
                Title=entry.find('title').string,
                Summary=entry.find('summary').string,
                ContentType=entry.find('content').get('type'),
                Content=html.unescape(entry.find('content').string),
                HtmlContent=html.unescape(entry.find('hatena:formatted-content', type='text/html').string),
                Categories=self.get_category_split_string(entry),
                IsDraft=self.get_draft_int_flag(entry),
                Edited=entry.find('app:edited').string,
                Published=entry.find('published').string,
                Updated=entry.find('updated').string
            ))
            print(self.db_entries['Entries'].find_one(EntryId=entry_id))
        else:
            print('{0}のレコードはすでに存在している。'.format(entry_id))
            print(self.db_entries['Entries'].find_one(EntryId=entry_id))

    def get_next_url(self, soup):
        link = soup.find('link', rel='next')
        if None == link:
            return None
        else:
            return link.get('href')
        
    def get_entry_id(self, entry, hatena_id, hatena_blog_id):
        entry_id = re.sub(r'tag:blog.hatena.ne.jp,[0-9]+:', "", entry.find('id').string)
        return entry_id.replace("blog-{0}-{1}-".format(hatena_id, hatena_blog_id), "")
        
    def get_category(self, entry):
        categories = []
        for cate in entry.find_all('category'):
            categories.push(cate.get('term'))
        return categories

    def get_category_split_string(self, entry):
        categories = ""
        for cate in entry.find_all('category'):
            categories = cate.get('term') + ','
        categories = categories[:-1]
        return categories

    def get_draft(self, entry):
        return entry.find('app:control').find('app:draft').string.lower()
        
    def get_draft_int_flag(self, entry):
        draft = entry.find('app:control').find('app:draft').string.lower()
        if ('yes' == draft):
            return 1
        elif ('no' == draft):
            return 0
        else:
            raise Exception('app:draftの値が想定外。:' + draft)

