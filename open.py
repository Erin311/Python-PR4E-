'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print 'Line Count:', count
'''
'''
fhand = open('mbox-short.txt')
for line in fhand:
	if line.startswith('From:') :
		print line
'''
'''
#Searching Through a File 
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:') :
		print line
'''
#Skipping with continue
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	#if not line.startswith('From:') :
	if not '@uct.ac.za' in line :  #Using in to select lines
		continue
	print line