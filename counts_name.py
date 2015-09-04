
'''
When we encounter a new name, we need to add a new entry in the
dictionary and if this the second or later time we have seen the name,
we simply add one to the count in the dictionary under that name
'''
'''
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
	if name not in counts:
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1
print counts
'''
#-----------------------------------------------------
#Simplified counting with get()
'''
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
	counts[name] = counts.get(name, 0) + 1
print counts
'''
#Counting Pattern
'''
counts = dict()
print 'Enter a line of text:'
line = raw_input('')
words = line.split()
print 'Words:', words
print 'Counting...'
for word in words:
	counts[word] = counts.get(word,0) + 1
print 'Counts', counts
'''
name = raw_input('Enter file:')
handle = open(name)
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print bigword, bigcount
