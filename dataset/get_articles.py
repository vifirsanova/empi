import requests
from bs4 import BeautifulSoup

a = 'https://aspergers.ru/node/' # the website I use
tag = [str(x) for x in range(101, 603)] # gen number of article I want to use
tag_ = [a+x for x in tag] # concat strings to get a list of pages with needed articles

pages = open('pages','w')

for elem in tag_: # iter articles
  r = requests.get(elem) # get request
  r.encoding = r.apparent_encoding # ensure encoding is right

  html = r.text # get content from a page
  soup = BeautifulSoup(html, "html.parser") # parse the page with BS
  temp = soup.body.get_text().strip() # get text from html as string

  pages.write(temp) # write text to file
  pages.write('\n')

pages.close()
