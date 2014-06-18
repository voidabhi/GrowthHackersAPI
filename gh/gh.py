#!/usr/bin/env python

"""
Growth Hackers API
Unofficial Python API for Growth Hackers

@author Abhijeet Mohan
@email void.aby@gmail.com
"""

import requests
from bs4 import BeautifulSoup

from utils import get_soup

class GH(object):
    """
	The class that parses the GH page, and builds up all articles
    """	
	
    def __init__(self):
		self.more=''
		
	def get_posts(self,trait='',limit=15):
		if limit == None or limit < 1 or limit > 30: #validate limit
			limit = 15
			
		if trait == 'trending' or trait not in ['latest','must-read','discussions','jobs','companies']:
			trait = ''
			
		posts = 0
		#fetch limit posts from the trait page
		while posts < limit :
			soup = get_soup(page=trait)
			print soup
			break
			
		#pass the soup to post factory object
	
	def __repr__(self):
		return '<GH object>'
		
		
		
		
class Post(object):
	"""
	The class represents a post in GH
	"""
	
	def __init__(self,title,date,category,author,type,link,details,comments):
		self.title = title
		self.category = category
		self.author = author
		self.type = type
		self.link = link
		self.details = details
		self.comments = comments
		
	@classmethod
	def from_soup(self,soup):
		pass
		
	def __repr__(self):
		return '<Post : {0}>'.format(self.title)

if __name__ == '__main__':
	print GH()
		