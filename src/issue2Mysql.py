import urllib
from bs4 import BeautifulSoup
import MySQLdb

conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '******', db = '******')

c = conn.cursor()

c.execute("CREATE TABLE issueIncludeContent (id varchar(16), type varchar(255), title text, content longtext)") # here content must be defined as longtext data ypte, because text data type in MySQL is smaller than some issue content in ceph

fr = open("issueLog.html", "r") # here must store html content in a html file. I originally store web scraped content into a .txt file. But format is ascii and not comply with html

soup = BeautifulSoup(fr.read())

count = 0
for title in soup.find_all("title"):
	count += 1
	print count
	subtitle = ['', '', '']
	title = title.get_text().encode('utf-8','replace')
	index1 = title.find("#")
	index2 = title.find(":")
	subtitle[0] = title[:index1]
	subtitle[1] = title[index1:index2]
	subtitle[2] = title[index2+1:]
	title_type = subtitle[0].strip(' ')
	title_id = subtitle[1].strip('#')
	title_text = subtitle[2]
	c.execute("INSERT INTO issueIncludeContent (id, type, title) VALUES (%s, %s, %s)", (title_id, title_type, title_text))

count = 0
for body in soup.find_all("body"):
	count += 1
	content = body.find(id = "main")
	content = content.get_text().encode('utf-8','replace')
	c.execute("UPDATE issueIncludeContent SET content=%s WHERE id=%s", (content, str(count)))

fr.close()

fr = open("issueLog7915.html", "r") # here must store html content in a html file. I originally store web scraped content into a .txt file. But format is ascii and not comply with html

soup = BeautifulSoup(fr.read())

count = 7914
for title in soup.find_all("title"):
	count += 1
	print count
	subtitle = ['', '', '']
	title = title.get_text().encode('utf-8','replace')
	index1 = title.find("#")
	index2 = title.find(":")
	subtitle[0] = title[:index1]
	subtitle[1] = title[index1:index2]
	subtitle[2] = title[index2+1:]
	title_type = subtitle[0].strip(' ')
	title_id = subtitle[1].strip('#')
	title_text = subtitle[2]
	c.execute("INSERT INTO issueIncludeContent (id, type, title) VALUES (%s, %s, %s)", (title_id, title_type, title_text))

count = 7914
for body in soup.find_all("body"):
	count += 1
	content = body.find(id = "main")
	content = content.get_text().encode('utf-8','replace')
	c.execute("UPDATE issueIncludeContent SET content=%s WHERE id=%s", (content, str(count)))

fr.close()

conn.commit()

conn.close()
