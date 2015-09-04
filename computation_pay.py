'''
Rewrite your pay computation to give the employee
1.5 times the hourly rate for hours worked above 40
hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
475 = 40 * 10 + 5 * 15

hours_user = int(raw_input('Enter Hours:'))
rate = int(raw_input('Enter Rate:'))
above_40_hours = 40
rate_in = 15
if hours_user > 40:
	plus = hours_user - 40
pay = above_40_hours * rate + plus * rate_in
print pay 
'''
#---------------------------------------------------------
'''
Rewrite your pay program using try and except so
that your program handles non-numeric input
gracefully.
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
'''
#Enter hours,rate with try/except
hours_user = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
try:
	aux_hours_user = int(hours_user)
	aux_rate = int(rate)
except:
	aux_hours_user = -1
	aux_rate = -1

if aux_hours_user > 0 or aux_rate > 0:
	above_40_hours = 40
	rate_in = 15
	if hours_user > 40:
		plus = aux_hours_user - 40
		pay = above_40_hours * aux_rate + plus * rate_in
	print pay 
else:
	print ("Error, please enter numeric input")