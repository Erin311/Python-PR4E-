name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sw = "From"
counts = dict()
lines = handle
for line in lines:
    if line.startswith(sw) and not line.startswith(sw+':'):
        line = ((line.rstrip()).lstrip()).split()
	counts[line[1]] = counts.get(line[1],0) + 1

def max(dictionary):
    max = None 
    highest = None
    #print dictionary
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    #print "new max is", max
	    highest = key
    return highest       

dictionary = counts
key = max(dictionary)
print key, dictionary[key] 