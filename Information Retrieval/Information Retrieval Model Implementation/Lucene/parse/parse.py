import urllib3
from bs4 import BeautifulSoup

quote_page = "https://lucene.apache.org/core/7_4_0/core/org/apache/lucene/index/package-summary.html"

http = urllib3.PoolManager()
response = http.request('GET', quote_page)
#soup = BeautifulSoup(response.data)
soup = BeautifulSoup(quote_page, 'html.parser')
print(soup.prettify())

