from ScrapeSearchEngine.ScrapeSearchEngine import Bing
from googlesearch import search as Google
import requests
from bs4 import BeautifulSoup

def q_Google(query):
    return [x for x in Google(query, tld= 'co.in', num= 10, stop= 10, pause= 10)]

def q_Bing(query):
    return Bing(query, '')

def get_text(url):
    output = ''
    blacklist = ['[document]', 'noscript', 'header', 'html', 'meta',
                'head', 'input', 'script', 'style']   

    for t in BeautifulSoup(requests.get(url).content, 'html.parser').find_all(text=True):
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    return output
