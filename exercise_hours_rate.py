#Exercise
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
