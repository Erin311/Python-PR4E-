#Using re.search() like find()
'''
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >= 0:
		print line
'''
'''
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line) :
		print line
'''
'''
#Using re.search() like startswith()
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:') :
		print line
'''
'''
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:', line) :
		print line		
'''
#Spam Confidence		
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)
print "Maximum:", max(numlist)

