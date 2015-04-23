'''
 This file export gitlog table in the database and create an adjacent matrix of each committed file
'''

import subprocess
import pprint
import MySQLdb
import csv

conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '******', db = '******')

c = conn.cursor()

query = "USE ceph;"
c.execute(query)
query = "SELECT commit_files FROM gitlog;"
c.execute(query)
rows = c.fetchall()

fileSet = set()

for row in rows:
	row = row[0]
	commfiles = row.strip('\n').split('\n')
	for commfile in commfiles:
		fileSet.add(commfile)

fileSet.remove('')
#print fileSet

AdjMatrix = {}


for keyo in fileSet:
	AdjMatrix[keyo] = {}
	for keyi in fileSet:
		AdjMatrix[keyo][keyi] = 0

for row in rows:
	row = row[0]
	commfiles = row.strip('\n').split('\n')
	if commfiles[0] is not '':
		for keyo in commfiles:
			for keyi in commfiles:
				AdjMatrix[keyo][keyi] += 1

#print AdjMatrix

with open('adjMatrix.csv', 'wb') as csvfile:
	writeCSV = csv.writer(csvfile, delimiter = ',')
	writeCSV.writerow([keys for keys in AdjMatrix])
	for keyo in AdjMatrix:
		writeCSV.writerow([AdjMatrix[keyo][keyi] for keyi in AdjMatrix[keyo]])

conn.commit()
