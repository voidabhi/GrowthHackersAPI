
from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from gh import Category

from bs4 import BeautifulSoup

import httpretty

class TestCategoryFromSoup(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://growthhackers.com/category/engagement/',body=get_content('gh_category.html'))

		self.category = Category.from_soup(BeautifulSoup(get_content('gh_category.html')))
	
	def test_article_author_fields(self):
		"""
			Testing GH Category
		"""
		self.assertEqual(self.category.cat_id,'engagement')
		self.assertEqual(self.category.title,'Engagement')
		self.assertEqual(self.category.url,'http://growthhackers.com?category_name=engagement')
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
