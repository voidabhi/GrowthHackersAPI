
from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from gh import Comment

from bs4 import BeautifulSoup

import httpretty

class TestCommentFromSoup(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://growthhackers.com/how-a-tiny-startup-used-reddit-to-build-an-army-of-1400-ambassadors-and-how-you-can-too/#comment-11694',body=get_content('gh_comment.html'))

		self.comment = Comment.from_soup(BeautifulSoup(get_content('gh_comment.html')))
	
	def test_comment_from_soup(self):
		"""
			Testing GH Category
		"""
		self.assertEqual(self.comment.cmt_id,'11694')
		self.assertEqual(self.comment.user,'everette')
		self.assertEqual(self.comment.datetime,'June 19, 2014 at 1:26 pm')
		self.assertEqual(self.comment.link,'http://growthhackers.com/how-a-tiny-startup-used-reddit-to-build-an-army-of-1400-ambassadors-and-how-you-can-too/#comment-11694')
		self.assertEqual(self.comment.content,'Wow so much value from a Subreddit, really insightful. You never know which channel is going to be effective for you.')
		self.assertEqual(self.comment.votes,'3')		
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
