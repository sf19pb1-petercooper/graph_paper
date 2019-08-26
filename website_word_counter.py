import requests
import pprint
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

r = requests.get("https://www.usatoday.com/story/news/politics/2019/08/26/donald-trump-china-trade-war/2118225001")
#print(r.content)

soup = BeautifulSoup(r.content, "html5lib")
#print(soup)

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
#print(text)

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (type(c.most_common()))

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(c.most_common())
