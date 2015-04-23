import urllib

#x = urllib.urlopen("https://www.google.com")

#print(x.read())
writeFile = open("issueLog.txt", "w")

for issueNum in range(1, 11235):
	print str(issueNum)
	url = 'http://tracker.ceph.com/issues/' + str(issueNum)
	x = urllib.urlopen(url)
	writeFile.write(x.read())

writeFile.close()
