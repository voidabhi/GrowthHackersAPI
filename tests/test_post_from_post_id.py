
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
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
