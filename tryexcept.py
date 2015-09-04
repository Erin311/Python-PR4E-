'''
try / except
When the first conversion fails - it
just drops into the except: clause
and the program continues

When the second conversion
succeeds - it just skips the except:
clause and the program continues

astr = 'Hello Bob'
try:
	istr = int(astr)
except:
	istr = -1
print 'First', istr
astr = '123'
try:
	istr = int(astr)
except:
	istr = -1
	
print 'Second', istr
'''
#example 
#First -1
#Second 123
#----------------------------------------------------------
'''
#sample try/except
rawstr = raw_input('Enter a number:')
try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0 :
	print 'Nice work'
else:
	print 'Not a number'
'''

largest = None
smallest = None
number = []
estado = True
while estado:
	num = raw_input("Enter a number: ")
	try:
		num1 = int(num)
	except:
		num1 = -1

	if num1 > 0:
		number.append(num1)
	else:
		print 'Invalid input'
		print 'Maximum',max(number)
		print 'Minimum',min(number)
		estado = False

















