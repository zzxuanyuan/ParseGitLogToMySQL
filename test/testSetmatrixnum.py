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
	if not commfiles:	# This line is to verify commfiles is not an empty string, 
						#otherwise, AdjMatrix[keyo][keyi] will report error since 
						#there is no hash for this empty string
		for keyo in commfiles:
			for keyi in commfiles:
				AdjMatrix[keyo][keyi] += 1

print AdjMatrix