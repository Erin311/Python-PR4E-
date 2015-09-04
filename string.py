# String 
'''
Using a while statement and
an iteration variable, and the
len function, we can
construct a loop to look at
each of the letters in a string
individually

fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print index, letter 
	index = index + 1

#Looping Through Strings
fruit = 'banana'
for letter in fruit:
	print letter
'''
'''
his is a simple loop that
loops through each letter in a
string and counts the number
of times the loop encounters
the 'a' character
'''
word = 'banana'
count = 0
for letter in word :
	if letter == 'a' :
		count = count + 1
print count

#https://docs.python.org/2/library/stdtypes.html#string-methods











