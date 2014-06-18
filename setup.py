
from setuptools import setup

setup(name='GrowthHacker',
      version='0.1',
	  install_requires=['BeautifulSoup4>=4.3.1', 'requests'],
      description='Python API for Growth Hackers',
	  long_description='Unofficial Python API for the blog http://growthhackers.com. Usage: https://github.com/voidabhi/GrowthHackersAPI',
      url='https://github.com/voidabhi/GrowthHackersAPI',
      author='Abhijeet Mohan',
      author_email='abhijeetshibu@gmail.com',
      license='MIT',
      packages=['gh','tests'],
	  test_suite='tests',
      zip_safe=False)