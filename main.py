#usaco contests download

import urllib2
from bs4 import BeautifulSoup

url='http://www.usaco.org/index.php?page=contests';
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

h2=soup.select(".panel h2")
for item in h2:	
	if item.string==' On-Line Contests ':
		break
	#here are useful data	
	season=item.string.split(':')[1].split(' ')[1]
	a=item.find_all('a')
	print(season)	
	print(a)