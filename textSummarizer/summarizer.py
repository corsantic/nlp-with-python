
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.bbc.com/news/technology-46516662')

soup  = bs.BeautifulSoup(source, 'lxml')