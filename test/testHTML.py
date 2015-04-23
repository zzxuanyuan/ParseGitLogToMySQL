import urllib
from bs4 import BeautifulSoup

fr = open("issueTest.html", "r") # here must store html content in a html file. I originally store web scraped content into a .txt file. But format is ascii and not comply with html
fw = open("issueTestOut.txt", "w")

soup = BeautifulSoup(fr.read())

fw.write(soup.get_text().encode('utf-8','replace')) # here must convert ascii format to utf-8 format

fr.close()
fw.close()

'''
for issueNum in range(1, 11):
	r = urllib.urlopen("http://tracker.ceph.com/issues/" + str(issueNum))
	soup =  BeautifulSoup(r.read())
#	title = soup.find_all("title")
#	print soup.title.string
	print soup.title.string
	print soup.

for title in soup.find_all("title"):
	print type(title)
	print title.string


print soup.prettify()



print soup.prettify()

title = soup.find_all("title")
print title
#print soup.title.string

for link in links:
	print link

#print soup

bugTitle = soup.title.text

if "Bug" in bugTitle:
	print type(bugTitle)
	print bugTitle
'''