



from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from gh import User

import httpretty

class TestUserFromUserId(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://growthhackers.com/member/everette/',body=get_content('gh_user.html'))

		self.author = User.from_user_id('everette')
	
	def test_user_from_id(self):
		"""
			Testing GH user
		"""
		self.assertEqual(self.author.user_id,'everette')
		self.assertEqual(self.author.name,'Everette Taylor')
		self.assertEqual(self.author.image_url,'http://1.gravatar.com/avatar/549a548591fabde9e0a3ec764eb39bf7?s=124&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D124&r=G')
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
