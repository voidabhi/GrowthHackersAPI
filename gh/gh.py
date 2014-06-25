#!/usr/bin/env python

"""
Growth Hackers API
Unofficial Python API for Growth Hackers

@author Abhijeet Mohan
@email void.aby@gmail.com
"""

import requests
from bs4 import BeautifulSoup
import re

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
		
		
class User(object):
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
		return User(user_id,name,image_url)
		
	def __repr__(self):
		return '<User : {0}>'.format(self.user_id)

class Category(object):
	"""
	The class represents a user in GH
	"""
	
	def __init__(self,cat_id,title,url):
		self.cat_id= cat_id
		self.title = title
		self.url = url
		
	@classmethod
	def from_soup(self,soup):
		cat_id = soup.find('a').get('href').split('=')[1]
		title = soup.find('a').contents[0]
		url = soup.find('a').get('href')
		return Category(cat_id,title,url)
		
	def __repr__(self):
		return '<Category : {0}>'.format(self.cat_id)

class Comment(object):
	"""
	The class represents a comment to a post in GH
	"""
	
	def __init__(self,cmt_id,datetime,user,link,content,votes):
		self.cmt_id= cmt_id
		self.user = user
		self.datetime = datetime
		self.link = link
		self.content = content
		self.votes = votes
		
	@classmethod
	def from_soup(self,soup):
		# parses a single li element in commentlist ul
		cmt_id = soup.find('li',class_='comment').get('id').split('-')[1]
		datetime = soup.find('span',class_='comment-meta').contents[0].strip()
		link= soup.find('span',class_='comment-meta').contents[1].get('href')
		 # extracting with regexp
		user_id = soup.find_all('cite',class_='fn')[1].contents[0]
		user = re.sub(r'[(@)]','',user_id)
		content = soup.find('div','comment-content').find('p').contents[0].strip()
		votes = soup.find('span',class_='com-score-%s'%cmt_id).contents[0]
		return Comment(cmt_id,datetime,user,link,content,votes)
	
		
	def __repr__(self):
		return '<Comment :#{0}>'.format(self.cmt_id)

class Post(object):
	"""
	The class represents a post in GH
	"""
	
	def __init__(self,id,title,url,date,category,author_id,votes,comments):
		self.id = id
		self.title= title
		self.url = url
		self.date = date
		self.category = category
		self.author = author_id
		self.votes = votes
		self.comments = comments
		
	@classmethod
	def from_post_id(self,post_id):
		soup = get_soup(page = post_id)
		title = soup.find('h1',class_='title post-item-title').find('a').contents[0]
		url = soup.find('h1',class_='title post-item-title').find('a').get('href')
		date = soup.find('span',class_='post-item-info').contents[0].split('in')[0].strip()
		category = Category.from_soup(soup.find('span',class_='post-item-info'))
		# todo = do this with regexp
		author_id = soup.find('a',{'rel':'author'}).get('href').split('/')[-2]
		votes = soup.find('div',class_='score2').find('p').contents[0]
		# todo = comments
		comments = ''
		return Post(post_id,title,url,date,category,author_id,votes,comments)
		
	def __repr__(self):
		return '<Post : {0}>'.format(self.id)		

if __name__ == '__main__':
	post = User.from_user_id('anand')
	print post