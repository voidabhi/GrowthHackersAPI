



from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from gh import User

import httpretty

class TestUserFromUserId(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://growthhackers.com/member/ryangum',body=get_content('gh_user.html'))

		self.author = User.from_user_id('ryangum')
	
	def test_article_author_fields(self):
		"""
			Testing article author
		"""
		self.assertEqual(self.author.user_id,'ryangum')
		self.assertEqual(self.author.name,'Ryan Gum')
		self.assertEqual(self.author.image_url,'http://1.gravatar.com/avatar/dbb480ad4b9d4592ea2dfb933498d89c?s=124&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D124&r=G')
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
