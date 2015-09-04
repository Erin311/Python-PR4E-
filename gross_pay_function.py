'''
hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
def computepay(hrs,rate):
    if hrs > 40:
        plus = hrs - 40
        pay = (40 * rate) + ((plus * rate) * 1.5)
    else:
        pay = hrs * rate
    return pay

p = computepay(hrs,rate)
print p
'''
n1 = int(raw_input("Enter n1:"))
n2 = int(raw_input("Enter n2:"))
def suma(n1,n2):
	s = n1 + n2 
	return s
a = suma(n1,n2)
print a