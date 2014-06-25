
import requests 
from bs4 import BeautifulSoup

from constants import BASE_URL

def get_soup(page=''):
	content = ''
	try:
		content = requests.get('%s/%s/' % (BASE_URL,page)).text
	except requests.exceptions.ConnectionError as e:
		content = requests.get('%s/%s' % (BASE_URL,page)).text
	finally:
		return BeautifulSoup(content.encode('utf8'))
		
		
	
def get_user_soup(user_id=''):
	"""
	Returns a bs4 object of the requested user
	"""
	return get_soup(page='member/%s'%user_id)