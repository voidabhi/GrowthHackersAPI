#!/usr/bin/env python

"""
Growth Hackers API
Unofficial Python API for Growth Hackers

@author Abhijeet Mohan
@email void.aby@gmail.com
"""

import requests
from bs4 import BeautifulSoup

class GH(object):
    """
    The class that parses the GH page, and builds up all articles
    """
	
	def __init__(self):
		pass
		
	def get_posts(self ,trait,limit=15):
        """
			Get all posts of given trait ('trending','latest','must read','jobs')
        """
		#validate limit
		#fetch limit posts from the trait page
		#pass the soup to post factory object
		pass
		
		
		
		
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
		