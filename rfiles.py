'''
xfile = open('mbox.txt')
for cheese in xfile:
	print cheese
'''
'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print 'Line Count:', count
'''
'''
#Searching Through a File
fhand = open('mbox.txt')
for line in fhand:
	if line.startswith('From:') :
		print line
'''
'''
fhand = open('mbox.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:') :
		print line
'''
'''
#Skipping with continue
fhand = open('mbox.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:') :
		continue
	print line
'''
'''
We can look for a string
anywhere in a line as our
selection criteria
#Using in to select lines

fhand = open('mbox.txt')
for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line :
		continue
	print line
'''
#Prompt for File Name
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
	if line.startswith('Subject:') :
		count = count + 1
print 'There were', count, 'subject lines in', fname

























