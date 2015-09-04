#guess number simple example
'''
rawstr = raw_input("Enter a number:")
try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0 :
	print ("Nice work")
else:
	print ("Not a number")
'''

'''
Rewrite your pay computation to give the employee
1.5 times the hourly rate for hours worked above 40
hours.
enter hours:45
enter rate:10
pay:475.0
'''

'''
hours = int(raw_input("Enter a number hours: "))
rate = int(raw_input("Enter a number rate: "))
if hours >= 40:
	pay = 40 * rate + 5 * 15

print ("you will to pay:" ,pay)
'''

x = int(raw_input("Enter a number x: "))
if x < 2 :
    print ("Below 2")
elif x >= 2 : 
    print ("Two or more")
else :
    print ("Something else")
 
