'''
 This file parse the git log file into MySQL database: ceph table: gitlog
'''

import subprocess
import pprint
import MySQLdb

conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '******', db = '****')

c = conn.cursor()

c.execute("CREATE TABLE gitlog (commit_id varchar(48), author varchar(32), date varchar(32), \
	commit_message varchar(255), commit_files text, patch_diff text)")

GIT_COMMIT_FIELDS = ['id', 'author_name', 'date', 'message', 'files', 'patches']

GIT_LOG_FORMAT = ['%H', '%an', '%ad', '%s']
GIT_LOG_FORMAT = '%x1e' + '%x1f'.join(GIT_LOG_FORMAT) + '%x1f'
p1 = subprocess.Popen('git log --name-only --format="%s" -3' %GIT_LOG_FORMAT, 
	shell = True, stdout = subprocess.PIPE)

p2 = subprocess.Popen('git log -p --format="%s" -3' %GIT_LOG_FORMAT, 
	shell = True, stdout = subprocess.PIPE)

(log1, _) = p1.communicate()
(log2, _) = p2.communicate()

log1 = log1.strip("\n\x1e").split("\x1e")
log2 = log2.strip("\n\x1e").split("\x1e")

log1 = [row.strip().split("\x1f") for row in log1]
log2 = [row.strip().split("\x1f") for row in log2]

count = 0
for count in range(len(log1)):
	log1[count].append(log2[count][len(log2[0])-1])
	query = [row for row in log1[count]]
	print query
	print len(query)
	print type(query[0])
	print count
	c.execute("INSERT INTO gitlog (commit_id, author, date, commit_message, commit_files, patch_diff) \
		VALUES (%s, %s, %s, %s, %s, %s)",
		(query[0], query[1], query[2], query[3], query[4], query[5]))

conn.commit()


