#!/usr/bin/env python

"""
Growth Hackers API
Unofficial Python API for Growth Hackers

@author Abhijeet Mohan
@email void.aby@gmail.com
"""

import requests
from bs4 import BeautifulSoup

from utils import get_soup , get_user_soup

class GH(object):
		"""
		The class that parses the GH page, and builds up all articles
		"""	
		
		def __init__(self):
			pass
			
		def get_posts(self,trait='',limit=15):
			if limit == None or limit < 1 or limit > 30: #validate limit
				limit = 15
				
			if trait == 'trending' or trait not in ['latest','must-read','discussions','jobs','companies']:
				trait = ''
				
			posts = 0
			#fetch limit posts from the trait page
			#while posts < limit :
			#	break
				
			#pass the soup to post factory object
		
		def __repr__(self):
			return '<GH object>'
		
		
class Author(object):
	"""
	The class represents a user in GH
	"""
	
	def __init__(self,user_id,name,image_url):
		self.user_id= user_id
		self.name = name
		self.image_url = image_url
		
	@classmethod
	def from_user_id(self,user_id):
		soup = get_user_soup(user_id)
		name = soup.find('h1',class_ = 'page-title').contents[0]
		image_url = soup.find('img',class_='avatar').get('src')
		return Author(user_id,name,image_url)
		
	def __repr__(self):
		return '<Author : {0}>'.format(self.user_id)		

if __name__ == '__main__':
	print Author.from_user_id('ryangum')