
import requests 
from bs4 import BeautifulSoup

from constants import BASE_URL

def get_soup(page=''):
    """
    Returns a bs4 object of the page requested
    """
    content = requests.get('%s/%s/' % (BASE_URL,page)).text
    return BeautifulSoup(content.encode('utf8'))

def get_article_soup(link):
    """
    Returns a bs4 object of the requested article
    """
    return get_soup(link)