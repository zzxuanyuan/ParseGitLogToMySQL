import csv

AdjMatrix = {}

AdjMatrix['file1'] = {}
AdjMatrix['file2'] = {}
AdjMatrix['file3'] = {}
AdjMatrix['file4'] = {}

AdjMatrix['file1']['file1'] = 0
AdjMatrix['file1']['file2'] = 0
AdjMatrix['file1']['file3'] = 0
AdjMatrix['file1']['file4'] = 0

AdjMatrix['file2']['file1'] = 0
AdjMatrix['file2']['file2'] = 0
AdjMatrix['file2']['file3'] = 0
AdjMatrix['file2']['file4'] = 0

AdjMatrix['file3']['file1'] = 0
AdjMatrix['file3']['file2'] = 0
AdjMatrix['file3']['file3'] = 0
AdjMatrix['file3']['file4'] = 0

AdjMatrix['file4']['file1'] = 0
AdjMatrix['file4']['file2'] = 0
AdjMatrix['file4']['file3'] = 0
AdjMatrix['file4']['file4'] = 0

rows = []

rows.append(('\n\nfile1\nfile2\nfile3\n',))
rows.append(('\n\nfile1\nfile2\nfile3\nfile4\n',))
rows.append(('\n\nfile1\nfile3\n',))
rows.append(('\n\nfile2\nfile3\n',))
rows.append(('\n\nfile1\nfile2\nfile3\n',))
rows.append(('\n\nfile1\nfile2\nfile3\nfile4\n',))
rows.append(('\n\nfile1\nfile2\nfile4\n',))
rows.append(('\n\n\n',))

print rows

for row in rows:
	row = row[0]
	commfiles = row.strip('\n').split('\n')
	print commfiles
	print type(commfiles)
	print type(commfiles[0])
	if commfiles[0] is not '':	# This line is to verify commfiles is not an empty string, 
						#otherwise, AdjMatrix[keyo][keyi] will report error since 
						#there is no hash for this empty string
		for keyo in commfiles:
			for keyi in commfiles:
				AdjMatrix[keyo][keyi] += 1

print AdjMatrix

with open('sample.csv', 'wb') as csvfile:
	writeCSV = csv.writer(csvfile, delimiter = ',')
	writeCSV.writerow(['keys'] + [keys for keys in AdjMatrix])
	for keyo in AdjMatrix:
		writeCSV.writerow([keyo] + [AdjMatrix[keyo][keyi] for keyi in AdjMatrix[keyo]])

