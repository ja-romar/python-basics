from bs4 import BeautifulSoup 
import requests

#download the content of webpage
url = "http://www.ibm.com"
#download the content in text format, store in variable 
data = requests.get(url).text

#create BS object
soup = BeautifulSoup(data, "html5lib")

#scrapp all links
for link in soup.find_all('a',href=True):
    print(link.get('href'))

#scrap all images Tags
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))