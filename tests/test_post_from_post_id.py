
from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from gh import Post

from bs4 import BeautifulSoup

import httpretty

class TestPostFromPostId(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://growthhackers.com/the-ultimate-customer-loyalty-guidebook-6000-words/',body=get_content('gh_post.html'))

		self.post = Post.from_post_id('the-ultimate-customer-loyalty-guidebook-6000-words')
	
	def test_post_from_post_id(self):
		"""
			Testing GH Post
		"""
		self.assertEqual(self.post.id,'the-ultimate-customer-loyalty-guidebook-6000-words')
		self.assertEqual(self.post.title,'The Ultimate Customer Loyalty Guidebook (6000 words)')
		self.assertEqual(self.post.url,'http://entrepreneurshipdaily.com/tips/how-to-increase-customer-retention-to-your-business/')
		self.assertEqual(self.post.date,'June 25, 2014')
		self.assertEqual(self.post.category.cat_id,'retention')
		self.assertEqual(self.post.author,'anand')
		self.assertEqual(self.post.votes,'5')
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
